from datetime import datetime, timedelta
from src.models.mode_model import Mode
from src.dto.sma_dto import SMADto
from src.dto.rl_dto import RLDto
from src.models.values_model import ValuesModel

class ModeController:


    @staticmethod
    def calculate_sma(mode: Mode) -> SMADto:
        lista = mode.inputs

        lista_amount : int = len(lista)
        total_of_sum_values : float = 0
        last_five_digits : float = 0
        to_promedy_low_sma : int = 5
        msg : str = ''
        for value in lista:
            total_of_sum_values += value.value

        for i in range(15, 20):
            print(lista[i].value)
            last_five_digits += lista[i].value
        #high and low SMA
        high_sma =   total_of_sum_values / lista_amount
        low_sma = last_five_digits / to_promedy_low_sma
        if low_sma > high_sma:
            msg = 'alcista'
        if low_sma < high_sma:
            msg = 'bajista'
        response = SMADto(high_sma,low_sma,msg)
        return response

    @staticmethod
    def calculate_rl(mode : Mode) -> RLDto:
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
        # formula: y = mx + b

        new_x = n+1 #21
        #y                mx     +   b
        future_value = (m * new_x) + b

        last_value = lista[-1].value

        if future_value > last_value:
            msg = 'el valor podria ser alcista'
        if future_value < last_value:
            msg = 'el valor podria ser bajista'


        response = RLDto(future_value, msg)
        return response

    @staticmethod
    def calculate_roc():
        pass