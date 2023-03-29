from api.database.schemas.tokens import tokens as collection


def get(address = None, *args, **kwargs):
    if address is None:
        return list(collection.find({}, {"_id": 0}))

    return collection.find_one({"address": address}, {"_id": 0})


def update(address, track, *args, **kwargs):
    return collection.update_one({"address": address}, {"$set": {"track": track}})


def insert(token, *args, **kwargs):
    return collection.insert_one(token)
