
#Напишите функцию hello_world, которая выводит строку 'Hello world!'. Вызовите эту функцию трижды.

def hello_world():
    print('hello_world')

hello_world()
hello_world()
hello_world()

#Напишите функцию my_sum, которая принимает два числа и возвращает их сумму. Проверьте корректность её работы при разных значениях аргументов. Например my_sum(1, 2), my_sum(25, 75) и т.д.
def my_sum(a,b):
    result = a+b
    return result

sum1= my_sum(2, 4)
sum2= my_sum (24, 75)

print (sum1)
print (sum2)

#Напишите функцию simple_compare, которая принимает два числа и возвращает True, если первое число меньше второго. Иначе возвращает False.
def simple_compare(a,b):
    if a<b:
        return True
    else:
        return False

result = simple_compare(2, 4)

print(result)

#OR
def simple_compare(a,b):
    return a<b

assert simple_compare(2,4)

#Напишите функцию compare, которая принимает два числа и возвращает -1 если первое число меньше второго, 1 если первое больше второго, и 0 если они равны.
def compare(a,b):
    if a<b:
        return 1
    elif a>b:
        return -1
    else:
        return 0

result = compare(2, 4)

print(result)

#Напишите функцию filter_negative_numbers, которая принимает список чисел, и возвращает новый список, составленный из элементов первого без отрицательных чисел,
def filter_negative_numbers(my_list):
    non_negative = []
    for i in my_list:
        if i >= 0:
            non_negative.append(i)
    return non_negative

my_list1 = [1, -2, 3, -4, 5, -6]
print (filter_negative_numbers(my_list1))