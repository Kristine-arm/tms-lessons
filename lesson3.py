import math

#TASK 1

a = input('write a number of the square:   ')
a = int(a)
print(4*a,  a**2,  a*math.sqrt(2))

#Task 2

x= input()
x= int(x)
if  x%2 ==0:
    print('true')
else:
    print ('false')

    OR

x = int(input("Enter a number: "))
print(x % 2 == 0)

Таsк3
#a=x*(1+10%)^y
x= float(input("enter the number"))
y=int(input ("enter the year"))
z=0.1
a= x*((1+z)**y)
print(a)

#Task4

x=input("enter the string")
y=tuple(set(x))
print(y)

#Task5

x=input("enter the month")
print(x)
y={'January': 31, 'February': 28,'March':31, 'April': 30, 'May': 31, 'June':30, 'July':31, 'August':31, 'September': 30, 'October':31, 'November': 30, 'december': 31 }
print(y.get(x))

Task6
x=input("enter the month")
z=int(input ("enter the number"))
y={'January': 31, 'February': 28,'March':31, 'April': 30, 'May': 31, 'June':30, 'July':31, 'August':31, 'September': 30, 'October':31, 'November': 30, 'december': 31 }
d=y.get(x)
print(z<d)