from src.models.user_model import User
from src.core.mongo_db import db
from src.schemas.user_shema import user_entity, users_entity
from src.dto.login_dto import UserDto
from src.dto.user_token_dto import UserTokenDto

class UserController:
    def __init__(self):
        pass

    @staticmethod
    def create_user( user: User) -> bool:
        try:
          new_user = dict(user)
          del new_user['id']
          use_id = db.users.insert_one(new_user).inserted_id
          db.users.find_one({'_id': use_id})
          print(user_entity(new_user))
          return True
        except Exception as e:
            print(f"error manito y tu error es {e}")
            return False


    @staticmethod
    def get_users() -> list:
        users = db.users.find()
        return users_entity(users)

    def update_user(self, user: User) -> bool:
        pass

    def delete_user(self, userid : str) -> bool:
        pass
    @staticmethod
    def find_user_by_id(userid : str) -> User:
        pass

    @staticmethod
    def login(login_data : UserDto) -> UserTokenDto | None:


            user_model = db.users.find_one({"email" : login_data.email , "password_hashed" : login_data.password_hashed})
            if not user_model :
                return None
            user_model["_id"] = str(user_model["_id"])
            user_token = UserTokenDto(user_model,'logica JWT')
            return user_token
