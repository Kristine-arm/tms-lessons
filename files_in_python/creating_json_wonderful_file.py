import json


import json
def write_json_file():
    with open ("_json_wonderful_file", "w") as file:
        animals = ["cat", "dog", "fish"]
        numbers = [1, 2, 3]
        contents = {animal: number for animal, number in zip (animals, numbers)}
        json.dump(contents, file)

write_json_file()



#example of writing json file(using dump) and reading (using load)
# import json
#
# # Example data
# data = {
#     "name": "John Doe",
#     "age": 30,
#     "city": "New York"
# }
#
# # Writing JSON data to a file using json.dump()
# with open('data.json', 'w') as file:
#     json.dump(data, file)
#
# # Reading JSON data from a file using json.load()
# with open('data.json', 'r') as file:
#     loaded_data = json.load(file)
#     print(loaded_data)  # This will print the Python dictionary loaded from the file