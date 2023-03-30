from api.database.db import db
from pymongo.collection import Collection


class Schema:
    def __new__(cls, coll_name, properties: dict, inserts: list = None) -> Collection:
        if coll_name in db.list_collection_names():
            return db[coll_name]

        coll = db.create_collection(coll_name, validator={
            '$jsonSchema': properties
            }
        )

        coll.insert_many(inserts)

        return coll