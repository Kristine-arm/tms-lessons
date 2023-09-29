#Задачи (1)
#Напишите функцию hello_world, которая печатает на экран приветствие "Hello world". Вызовите написанную функцию.

def hello_world():
    print('hello_world')

hello_world()

#Напишите функцию hello_world, которая возвращает строку "Hello world". Вызовите написанную функцию и выведите результат на экран.
def hello_world():
    return 'hello_world'

print (hello_world())

#Напишите функцию hello, которая принимает на вход строку (имя) и выводит на экран фразу "Hello {имя}". Вызовите написанную функцию.
def hello(name):
    print (f'hello {name}')

hello('Ania')


#Напишите функцию hello, которая принимает на вход строку (имя) и возвращает строку "Hello {имя}". Вызовите написанную функцию и выведите результат на экран.
def hello(name):
    return (f'hello  + {name}')

#print (hello('Ania'))

Задачи (2)
#Напишите функцию is_palindrome, которая принимает на вход строку, и возвращает True если это палиндром, иначе False.
def is_palindrome(s):
    return s == s[::-1]
    if s==s[::-1]:
        print ('True')
    else:
        print ('False')


print(is_palindrome('dddt'))

#Напишите функцию list_sum, которая принимает на вход список и возвращает сумму элементов списка. Использование встроенной функции sum запрещено.
def list_sum (my_list):
    result=0
    for i in my_list:
        result+=i
    return result

my_list1 =[6,7,8,9]
print (list_sum (my_list1))

#Создать функцию sum_and_max, которая принимает на вход неопределенное количество аргументов и возвращает их сумму и максимальное из них. Использовать встроенные sum и max разрешено.

def sum_and_max (my_list):
    return sum(my_list), max (my_list)

my_list_666 =[6,7,8,9]
my_variable = sum_and_max (my_list_666)
print (my_variable)

#Напишите функцию my_round, аналог встроенной round (ссылка на документацию). Использование самой функции round запрещено.
#sxal e, noric grel
def my_round(n, digits=0):
    n*=10**digits
    fraction n%1
    n=int(n)
    if fraction >=0.5:
        n+=1
        n/=10**digits
    return n

#Напишите функцию get_natural_numbers, которое принимает целое число n и возвращает список натуральных чисел от 1 до n включительно. Используйте генераторы списков.
def get_natural_numbers (n):
    if n<1:
        return []
    else:
        natural_numbers = [i for i in range (1, n+1)]
        return natural_numbers

print (get_natural_numbers(6))

#Напишите функцию filter_odd_numbers, которая принимает на вход список целых чисел и возвращает новый список, состоящий из элементов первоначального, но без нечётных чисел.
def get_odd_numbers(my_list):
    odd_list= []
    for i in my_list:
        if i%2==1:
            odd_list.append(i)
    return odd_list

my_list1= [1, 2, 3, 4, 5, 6]
print (get_odd_numbers(my_list1))

