import json

data={'name': 'Kristine', 'Surname': 'Sargsyants', 'Nationality': 'Armenian'}
with open ('file_03.json', 'w') as file:
    json.dump(data, file)