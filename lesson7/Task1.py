#Пользователь вводит произвольное количество латинских букв через пробел. Буквы могут быть как в верхнем, так и в нижнем регистре (на результат работы это влиять не должно).
#Напишите функцию map_to_tuples, которая принимает список из этих букв и возвращает список из кортежей. В каждом кортеже первой должна идти буква в верхнем регистре, а второй эта же буква в нижнем.
#Выведите результат работы функции на экран.

def map_to_tuple(l: list[str])-> list[tuple]:
    a=list(map(lambda x: (x.upper(), x.lower()), l))
    return a
my_list=input().split()
print (map_to_tuple(my_list))

#with for loop
def input_list_with_simple_cycle() -> list[int]:
    input_strings = input().split()
    input_numbers: list[int] = []
    for s in input_strings:
        input_numbers.append(int(s))
    return input_numbers

print(input_list_with_simple_cycle())

#with list generator
from typing import List

def input_list_with_generator() -> List[int]:
    return [int(s) for s in input().split()]

print(input_list_with_generator())
