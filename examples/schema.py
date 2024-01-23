sc_exam = {
    "properties": {
        "user_oid": {
            "type": "string",
            "title": "user_oid"
        },
        "name": {
            "title": "Name",
            "type": "string"
        },
        "address": {
            "title": "Address",
            "type": "integer"
        },
        "is_b": {
            "title": "Is B",
            "type": "boolean"
        },
        "loda": {
            "type": "string",
            "title": "loda"
        },
        "dict": {
            "type": "object",
            "title": "Dict",
            "properties": {
                "class": {
                    "title": "class",
                    "type": "string",
                    "classifficator_id": "65a4b0782ecadf80709dcc2a"
                },
                "value": {
                    "title": "class_value",
                    "type": "integer"
                }
            },
            "required": [
                "class",
                "value"
            ]
        },
        "li": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "title": "id"
                    },
                    "name": {
                        "type": "string",
                        "title": "name"
                    },
                    "test": {
                        "type": "string",
                        "title": "looss"
                    }
                },
                "required": [
                    "id",
                    "name"
                ],
                "title": "JSON списка"
            },
            "title": "list"
        },
        "тест": {
            "type": "string",
            "title": "Тестовое поле"
        },
        "Справочник районов": {
            "type": "object",
            "title": "Районы",
            "properties": {
                "class": {
                    "type": "string",
                    "classifficator_id": "65a4dcf7b5aa5883a6faf3c6"
                },
                "value": {
                    "type": "integer"
                }
            },
            "required": [
                "class",
                "value"
            ]
        }
    },
    "required": [
        "name",
        "address",
        "is_b",
        "loda",
        "dict",
        "li",
        "тест",
        "Справочник районов",
        "user_oid"
    ],
    "title": "TestSchema",
    "type": "object",
    "contest_oid": "65a767c72e0fe1554e0d3c9a"
}
