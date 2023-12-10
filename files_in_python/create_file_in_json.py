import json

def write_to_json():
    name = "Kristine"
    animal = "Сокол"
    age = "10000"

    data = {
        "name": name,
        "animal": animal,
        "age": age
    }

    file_path = "file.json"

    with open(file_path, "w") as file:
        json.dump(data, file)

write_to_json()