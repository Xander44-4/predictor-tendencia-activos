def user_entity(entity) -> dict:
    return {
        "id" : str(entity["_id"]),
        "username": entity["username"],
        "email": entity["email"],
        "password_hashed": entity["password_hashed"],
    }
def users_entity(entity) -> list:
   return [user_entity(entity) for entity in entity]