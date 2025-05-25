from datetime import datetime, date
from typing import List
from src.models.mode_model import Mode
from src.dto.sma_dto import SMADto
from src.dto.rl_dto import RLDto
from src.dto.roc_dto import ROCdto
from src.models.values_model import ValuesModel
from src.schemas.mode_shema import mode_entity
from src.core.mongo_db import db


def to_db(mode_type: int, user_id: str, inputs: list, answer_type, mode: Mode) -> str:
    try:
        mode.mode_type = mode_type
        mode.userId = user_id
        mode.inputs = [ValuesModel(**item) if not isinstance(item, ValuesModel) else item for item in inputs]
        mode.answer_mode = answer_type

        mode_to_db = mode.model_dump(exclude={"id"})

        # Convertir datetime.date a string 'YYYY-MM-DD' para MongoDB
        for input_item in mode_to_db["inputs"]:
            if isinstance(input_item["datetime"], date):
                input_item["datetime"] = input_item["datetime"].isoformat()

        db.modes.insert_one(mode_to_db)

    except Exception as e:
        print('Error sending the information to DB', e)

    return 'añadido correctamente'

class ModeController:


    @staticmethod
    def calculate_sma(mode: Mode, user_id : str) -> SMADto:
        lista = mode.inputs

        lista_amount : int = len(lista)
        total_of_sum_values : float = 0
        last_five_digits : float = 0
        to_promedy_low_sma : int = 5
        msg : str = ''
        for value in lista:
            total_of_sum_values += value.value

        for i in range(15, 20):

            last_five_digits += lista[i].value
        #high and low SMA
        high_sma =   total_of_sum_values / lista_amount
        low_sma = last_five_digits / to_promedy_low_sma

        if low_sma > high_sma:
            msg = 'alcista'
        if low_sma < high_sma:
            msg = 'bajista'

        response = SMADto(
            high_sma=high_sma,
            low_sma=low_sma,
            msg=msg
        )
        mode.answer_mode = response
        to_db(1,user_id,lista,response,mode)
        return response

    @staticmethod
    def calculate_rl(mode : Mode, user_id : str) -> RLDto:
        lista = mode.inputs
        msg = ''
        n = len(lista)
        list_of_x = []
        x = 0
        y = 0
        xy = []
        sum_of_xy = 0
        x_elevate_two = []
        sum_of_x_elevate_two = 0

        #bucle para sumar los valores de la lista list_of_x 1 por 1
        for i, value in enumerate(lista, start=1):
            list_of_x.append(i)

        for i, values in enumerate(lista, start=1):
            x = sum(list_of_x)
            y += values.value
            xy.append(list_of_x[i-1] * values.value)
            x_elevate_two.append(list_of_x[i-1] ** 2)

        for values in xy:
            sum_of_xy += values

        for values in x_elevate_two:
            sum_of_x_elevate_two += values

        mega_formula_pendient = (  ((x * y) / n) - sum_of_xy  )  / ( ((x ** 2) / n) - sum_of_x_elevate_two ) #formula de la pendiente
        m = mega_formula_pendient

        x_to_pendient = x / n
        y_to_pendient = y / n

        # y - m * x
        formula_of_b = y_to_pendient - (m * x_to_pendient)
        b = formula_of_b


        new_x = n+1 #21
        #y                mx     +   b
        future_value = (m * new_x) + b

        last_value = lista[-1].value

        if future_value > last_value:
            msg = 'el valor podria ser alcista'
        if future_value < last_value:
            msg = 'el valor podria ser bajista'


        response = RLDto(future_value, msg)
        to_db(2,user_id,lista,response,mode)

        return response

    @staticmethod
    def calculate_roc(mode: Mode, user_id : str,period: int = 5, ) -> List[ROCdto]:
        lista = mode.inputs
        list_roc: List[ROCdto] = []

        for i in range(len(lista)):
            current_value = lista[i].value
            if i < period:
                roc = "n/a"
            else:
                previous_value = lista[i - period].value
                if previous_value != 0:
                    roc = round(((current_value / previous_value) - 1) * 100, 2)
                else:
                    roc = "n/a"

            dto = ROCdto(t=i, price=current_value, roc=roc)
            list_roc.append(dto)

        to_db(3, user_id, lista, list_roc, mode)
        return list_roc

