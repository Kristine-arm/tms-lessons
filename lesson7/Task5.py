#Напишите функцию-декоратор my_decorator, в которую можно обернуть функцию, которая принимает один входной параметр.
#Ваш декоратор должен будет выводить в консоль входной параметр оборачиваемой функции, запускать функцию, а затем выводить результат этой функции.

def my_decorator(func):
    def wrapper(x):
        print(f'Input: {x}')
        result = func(x)
        print(f'Result:{result}')
        return result
    return wrapper

@my_decorator
def square(x):
    return x**2

y=square(5)
print(f'y={y}')

