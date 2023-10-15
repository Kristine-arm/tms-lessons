#Решите прошлую 5 задачу так, чтобы ваш декоратор работал для любой функции, с любым количеством параметров. А также чтобы работало с именованными параметрами.
#Подсказка: используйте *args и **kwargs.
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Input: {args}{kwargs}')
        result = func(*args, **kwargs)
        print(f'Result:{result}')
        return result
    return wrapper

@my_decorator
def square(x):
    return x**2

y=square(5)
print(f'y={y}')
