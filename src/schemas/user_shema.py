def user_entity(item) -> dict:
    return {
        "id" : str(item["_id"]),
        "username": item["username"],
        "email": item["email"],
        "password_hashed": item["password_hashed"],
    }
def users_entity(entity) -> list:
   return [user_entity(item) for item in entity]