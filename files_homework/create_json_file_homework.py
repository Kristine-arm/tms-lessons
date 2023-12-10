import json
def read_simple_list(adress, standard_of_characters='utf-8'):
    with open(adress, encoding = standard_of_characters) as file:
        some_list = file.read().splitlines()

        names = []
        surnames = []

        for person in some_list:
            new_list = person.split(',')
            names.append(new_list[0])
            surnames.append(new_list[1])

    return names,surnames

names, surnames = read_simple_list('C:/Users/TOSHIBA TOUCHSCREEN/Desktop/TML lessons downloads/abc.txt')

print(names)
print(surnames)

def write_json_file(list_for_names, list_for_surnames):
    with open("C:/Users/TOSHIBA TOUCHSCREEN/Desktop/TML lessons downloads/harry_poter.json", "w") as file:
        contents = {name_of_character : surname_of_the_character for name_of_character, surname_of_the_character in zip(list_for_names, list_for_surnames)}
        json.dump(
            contents,
            file,
            sort_keys=True,
            ensure_ascii=False,
            indent=4,
        )

write_json_file(names, surnames)