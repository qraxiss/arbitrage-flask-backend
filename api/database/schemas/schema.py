from api.database.db import db
from pymongo.collection import Collection


class Schema:
    def __new__(cls, coll_name, properties: dict) -> "Collection":
        if coll_name in db.list_collection_names():
            return db[coll_name]

        return db.create_collection(coll_name, validator={
                '$jsonSchema': properties
                }
            )
