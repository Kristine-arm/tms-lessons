#Пользователь вводит произвольное количество слов через пробел. Затем (на следующей строке) вводит один символ (разделитель).
#Вам нужно написать функцию my_join, которая принимает список из строк и символ-разделить, и возвращает строку, в которой все слова из списка соединены через символ разделитель.
from functools import reduce
def my_join(l: list[str], delimeter: str)->str:
    return reduce(lambda x, y: x + delimeter + y,  l)

my_list= input().split()
delimeter= input()
print(my_list(my_join, delimeter))

#with for loop
def my_join(word_list, delimiter):
    result = ''
    for word in word_list:
        result = result + word + delimiter
    if result.endswith(delimiter):
        result = result[:-len(delimiter)]
    return result

input_words = input("Enter words separated by space: ").split()
delimiter = input("Enter a delimiter: ")

joined_string = my_join(input_words, delimiter)

print(joined_string)





