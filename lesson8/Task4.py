import json

name=input('write the name   ')
surname=input('write the surname   ')
age=input('write the age   ')

person = {'name': name, 'surname': surname, 'age': age}

with open ('file_04.json', 'w') as file:
    json.dump(person, file)

