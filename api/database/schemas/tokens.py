from api.database.schemas.schema import Schema
from json import load

tokens = Schema(coll_name='tokens',
                properties={
                    "type": "object",
                    "properties": {
                        "pair": {},
                        "address": {
                            "type": "string",
                        },
                        "decimals": {
                            "bsonType": "int",
                            "minimum": 0
                        },
                        "symbol": {
                            "type": "string",
                        },
                        "name": {
                            "type": "string",
                        },
                        "track": {
                            "type": "boolean"
                        }
                    },
                    "required": ["pair", "address", "decimals", "symbol", "name", "track"],
                    "additionalProperties": True
                },
                inserts=load(open('tokens.json', 'r')))
