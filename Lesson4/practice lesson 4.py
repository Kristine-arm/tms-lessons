#Посчитайте сумму чисел от 0 до 100 (включительно).

x=0
for i in range (0, 101):
    x+=i
print (x)

#Посчитайте сумму чисел от 100 до 1000 (включительно)

x=100
for i in range (100, 1001):
    x+=i
print (x)

#Посчитайте сумму чётных чисел от 100 до 1000 (включительно)

x=100
for i in range(100, 1001, 2):
    if x % 2 == 0:
        x+=i
print(x)

#Посчитайте факториал числа 10 (т.е. 1 * 2 * 3 * ... * 10)

x=1
for i in range(1,11):
    x*=i
print(x)

#Посчитайте выражение 2**10 не используя оператор **

x=2
for i in range(1,11):
    x*=2
print(x)

#Пользователь вводит число. Посчитайте сумму цифр этого числа.
#Количество цифр числа может быть произвольными
#15 -> 1 + 5 = 6

a=input('write number    ')
a = list(a)
x = 0
for i in range (len(a)):
    x+=int(a[i])
print(x)

#Программа загадывает случайное число от 1 до 5.
#Пользователь пытается угадать, вводя числа.
#Если пользователь угадал - выведите поздравление и завершите программу.
#Если не угадал - программа предлагает попробовать ещё раз до тех пор, пока пользователь не угадает.

import random
hiden_number = random.randint(0, 5)

while True:
    user_number = int(input("Guess the number between 0 and 5: "))

    if user_number == hiden_number:
        print('Congrats')
        break
    else:
        print("wrong, try again")

#Вычисляйте сумму натуральных чисел до тех пор, пока сумма не окажется больше 1000. Выведите получившуюся сумму и последнее натуральное число, вошедшее в него.

x=0
for i in range (1000):
    if x+i<1000:
        x+=i
    else:
        print(i)
        break
print(x)