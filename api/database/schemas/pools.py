from api.database.schemas.schema import Schema

pool = {
    "type": "object",
    "properties": {
        "swap": {
            "type": "string"
        },
        "version": {
            "bsonType": "int"
        },
        "fee": {
            "bsonType": "int"
        },
        "t0": {
            "type": "string"
        },
        "t1": {
            "type": "string"
        },
        "buy": {
            "type": "number"
        },
        "sell": {
            "type": "number"
        }
    },
    "required": ["buy", "sell", "swap", "version", "fee"],
}

pools = Schema(coll_name='pools',
               properties=pool)
