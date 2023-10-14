#Даны два числа, если они равны выведите yes, иначе - no.
a=int(input('write a number   '))
b=int(input('write a number   '))
if a==b:
    print('yes')
else:
    print('no')

#Даны два числа, вывести на экран максимальное из них.
a=int(input('write a number   '))
b=int(input('write a number   '))

if a>b:
    print (a)
else:
    print (b)

#Дано число. Если оно положительно выведите yes, иначе no.
a=int(input('write a number   '))
if a>0:
    print ('yes')
else:
    print ('no')

#Дано число. Если оно положительно - выведите positive, если отрицательно - negative, если равно нулю - zero.

a=int(input('write a number   '))
if a>0:
    print ('yes')
elif a==0:
    print ('zero')
else:
    print ('no')

#Даны три числа. Если они все больше 0 - вывести yes, иначе - no.
a=int(input('write a number   '))
b=int(input('write a number   '))
c=int(input('write a number   '))

if a>0 and b>0 and c>0:
    print ('yes')
else:
    print ('no')

#Дан номер месяца (число от 1 до 12). Выведите пору года, которой этот месяц принадлежит: зима, весна, лето или осень.
a=int(input('write a number from 1 to 12  '))
if a in (3, 4, 5):
    print ('Spring')
elif a in (6,7,8):
    print ('summer')
elif a in (9,10,11):
    print ('fall')
else:
    print('winter')

#Дано три числа. Вывести количество положительных чисел среди них.
a = int(input('write a number   '))
b = int(input('write a number   '))
c = int(input('write a number   '))
x = 0
if a > 0:
    x += 1
if b > 0:
    x += 1
if c > 0:
    x += 1

print(x)

#Даны три числа, выведите максимальное из них (не используя функцию max и не создавая дополнительных переменных и сделав не более 2 сравнений для нахождения результата).
a = int(input('write a number   '))
b = int(input('write a number   '))
c = int(input('write a number   '))

if a>b and a>c:
    print (a)
if b>c and b>a:
    print (b)
else:
    print (c)