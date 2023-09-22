x=input("enter the month   ")
z=int(input ("enter the number   "))
y={'January': 31, 'February': 28,'March':31, 'April': 30, 'May': 31, 'June':30, 'July':31, 'August':31, 'September': 30, 'October':31, 'November': 30, 'december': 31 }
d=y.get(x)
print(z<d)