import json

DB_FILE = "db.json"


def read_db():
    try:
        with open(DB_FILE, "r") as file:
            # Json.load Transforme le json en dictionnaire python
            return json.load(file)
    except FileNotFoundError:
        return {"projects": []}


def write_db(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)
