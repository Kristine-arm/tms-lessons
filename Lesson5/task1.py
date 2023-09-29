#Напишите функцию is_year_leap, которая принимает число (год) и возвращает True если год високосный (см. комментарий к слайда), False если нет.

def is_year_leap (n):
    if n%4==0:
        return ("true")
    else:
        return ('false')

print (is_year_leap (2012))
