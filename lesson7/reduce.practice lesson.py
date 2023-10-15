#Дан список чисел. Найти его сумму.
from functools import reduce

def input_list():
    a = input().split()
    a = [int(x) for x in a]
    result = reduce(lambda x, y: x + y, a)
    return result

print(input_list())

#with for loop
def input_list():
    values = input().split()
    values = [int(x) for x in values]
    total = 0

    for i in values:
        total += i

    return total

print(input_list())

#Дан список чисел. Найти минимальное число.
from functools import reduce
def input_list():
    a = input().split()
    a = [int(x) for x in a]

    # Use reduce to find the minimum value
    result = reduce(lambda x, y: x if x < y else y, a)

    return result

print(input_list())

#with for loop
def input_list():
    values = input().split()
    values = [int(x) for x in values]
    min_value = values[0]

    for i in values:
        if i < min_value:
            min_value = value

    return min_value

print(input_list())

#Дан список чисел. Найти произведение всех элементов.
from functools import reduce
def input_list():
    a = input().split()
    a = [int(x) for x in a]
    result = reduce(lambda x, y: x * y, a)
    return result

print(input_list())

#with for loop
def input_list():
    values = input().split()
    values = [int(x) for x in values]
    total = 1

    for i in values:
        total *= i

    return total

print(input_list())

#С помощью функции reduce и range найти факториал числа 5.
from functools import reduce
def input_list():
    a = 5
    a = [int(x) for x in range(1,6)]
    result = reduce(lambda x, y: x * y, a)
    return result

print(input_list())

#with for loop
def input_list():
    a=input('napisz tylko jedna liczbe')
    a = int(a)
    total = 1

    for i in range(1,a+1):
        total *= i

    return total

print(input_list())

# Напишите свою реализацию функции my_reduce. Для простоты можно сделать третий параметр обязательным
#square(reduce need always 2 arguments, that is why, we need xand y)
from functools import reduce

def input_list():
    numbers = input('Write numbers with space: ').split()
    numbers = [int(x) for x in numbers]
    result = reduce(lambda x, y: x * y, [num**2 for num in numbers])
    return result

print(input_list())

#with for loop
def input_list():
    numbers = input('Write numbers with space: ').split()
    numbers = [int(x) for x in numbers]
    result=1
    for i in numbers:
        result*=i**2
    return result

print(input_list())


