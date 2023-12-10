def write_simple_file():
    with open ("_txt_write_txt", "w") as file:
        for number in range (10):
            file.write(f"{number}\n")

write_simple_file()
