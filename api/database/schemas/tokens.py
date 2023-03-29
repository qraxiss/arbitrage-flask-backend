from api.database.schemas.schema import Schema

tokens = Schema(coll_name='tokens',
                properties={
                    "type": "object",
                    "properties": {
                        "pair": {
                            "type": "string",
                        },
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
                }
                )
