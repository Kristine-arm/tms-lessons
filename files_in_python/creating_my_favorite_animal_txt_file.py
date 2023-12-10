def write_to_file():
    content = ["Kristine\n","dog\n","12\n"]
    file_path = "my_favorite_animal.txt"

    with open(file_path, "w") as file:
        file.writelines(content)

write_to_file()
