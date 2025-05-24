
def mode_entity(entity) ->dict:
    return {
        "id" : str(entity["_id"]) ,
        "mode_type" : entity["mode_type"],
        "user_id" : entity["userId"],
        "inputs" : [input_item.dict() for input_item in entity["inputs"]],
        "answer_mode" : entity["answer_mode"]
    }
