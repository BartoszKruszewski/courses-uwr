books_validator = {
  "$jsonSchema": {
    "bsonType": "object",
    "required": ["id", "title", "author", "copies"],
    "properties": {
      "id": {
        "bsonType": "int",
        "description": "must be an integer"
      },
      "title": {
        "bsonType": "string",
        "description": "must be a string"
      },
      "author": {
        "bsonType": "string",
        "description": "must be a string"
      },
      "copies": {
        "bsonType": "array",
        "description": "must be an array",
        "items": {
          "bsonType": "object",
          "required": ["copy_id", "status"],
          "properties": {
            "copy_id": {
              "bsonType": "string",
              "description": "must be a string"
            },
            "status": {
              "enum": ["available", "borrowed"],
              "description": "must be either 'available' or 'borrowed'"
            }
          }
        }
      }
    }
  }
}

readers_validator = {
  "$jsonSchema": {
    "bsonType": "object",
    "required": ["id", "name", "borrowings"],
    "properties": {
      "id": {
        "bsonType": "string",
        "description": "must be a string"
      },
      "name": {
        "bsonType": "string",
        "description": "must be a string"
      },
      "borrowings": {
        "bsonType": "array",
        "description": "must be an array",
        "items": {
          "bsonType": "object",
          "required": ["copy_id", "borrow_date"],
          "properties": {
            "copy_id": {
              "bsonType": "string",
              "description": "must be a string"
            },
            "borrow_date": {
              "bsonType": "date",
              "description": "must be a date"
            },
            "return_date": {
              "bsonType": ["date", "null"],
              "description": "must be a date or null"
            }
          }
        }
      }
    }
  }
}


