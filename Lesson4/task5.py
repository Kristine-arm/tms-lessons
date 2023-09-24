x= int(input("enter the number   "))
a=x%10
b=x//10
b=  list(str(b))
y=0
for i in range (len(b)):
    y+=int(b[i])
print(a+y)


