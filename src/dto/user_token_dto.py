from src.models.user_model import User


class UserTokenDto:
    def __init__(self,user_data:User, token: str):
        self.user_data = user_data
        self.token = token
