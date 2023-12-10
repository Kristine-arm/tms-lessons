import json


def read_simple_list():
    with open("_txt_read.txt") as file:
        some_list = file.read().splitlines()
    print(some_list)


def read_separated_values():
    with open("_separated_list.csv") as file:
        lines = file.read().splitlines()
        split_lines = [line.split(",") for line in lines]
        print(split_lines)
        # split_lines = []
        # for line in lines:
        #     split_line = line.split(",")
        #     split_lines.append(split_line)


def read_json_file():
    with open("_json_read.json") as file:
        json_contents = json.load(file)
    print(json_contents)


def write_simple_file():
    with open("_txt_write.txt", "w") as file:
        for number in range(10):
            file.write(f"{number}\n")


def write_json_file():
    with open("_json_write.json", "w") as file:
        animals = ["барсук", "racoon", "opossum"]
        numbers = [1, 2, 3]
        contents = {animal: number for animal, number in zip(animals, numbers)}
        # some_dict = {}
        # for animal, number in zip(animals, numbers):
        #     some_dict.update({animal: number})
        json.dump(
            contents,
            file,
            sort_keys=True,
            ensure_ascii=False,
            indent=4,
        )


def write_json_file_2():
    with open("My_information.json", "w") as file:
        list_a = ["name", "animal", "age"]
        list_b = ["Nika", "Кошка", "69"]
        contents = {animal: number for animal, number in zip(list_a, list_b)}
        json.dump(
            contents,
            file,
            sort_keys=True,
            ensure_ascii=False,
            indent=4,
        )

import json
def add_favorite_movie_to_json(Whatever):
    file_path = "file.json"

    with open(file_path, "r") as file:
        data = json.load(file)

    data["favorite_movie"] = Whatever

    with open(file_path, "w") as file:
        json.dump(data, file)



if __name__ == "__main__":
    pass
    read_simple_list()
    read_separated_values()
    read_json_file()
    write_simple_file()
    write_json_file()
    write_json_file_2()
    add_favorite_movie_to_json("hello")