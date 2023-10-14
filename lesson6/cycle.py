#Посчитайте сумму чисел от 1 до 10. (ответ: 55)

x=0
for i in range (1,11):
    x+=i

print (x)

#Дан список чисел. Найти их сумму.
my_list= [1, 2, 3]
x=0
for i in my_list:
    x+=i

print (x)

#Дан список чисел. Найти их максимальное среди них.
my_list= [1, 2, 3]
m=my_list[0]
for i in my_list:
    if  i>m:
        m=i

print (m)

#Дан список чисел. Если среди них есть ноль - вывести yes, иначе no.
my_list= [1, 0, 3]
count = 0
for i in my_list:
    if i==0:
        count+=1

if count>0:
    print ('yes')
else:
    print ('no')

#Дана строка. Посчитайте сколько раз в ней встречается символ "a".

my_list= 'andzej'
count = 0
for i in my_list:
    if i.lower()=='a':
        count+=1

print (count)

# Дан словарь "слово" -> число. Вывести максимальное число среди значений словаря. Пример: {'a': 1, 'b': 2} -> 2.
my_dict = {'word_a': 1, 'word_b': 2, 'word_c': 5, 'word_d' : 1}

items_view = my_dict.items()
my_list= []
for key, value in items_view:
    my_list.append(value)

print(max(my_list))

#OR
my_dict = {'word_a': 1, 'word_b': 2, 'word_c': 5, 'word_d' : 1}

max_value = max(my_dict.values())

print (max_value)


#Дан словарь "слово" -> число. Вывести ключ, соответствующий максимальному значению.

my_dict = {'word_a': 1, 'word_b': 2, 'word_c': 5, 'word_d' : 1}
x = my_dict.items()

max_value = max(my_dict.values())

max_key= None
for key, value in my_dict.items():
    if value == max_value:
        max_key=key
if max_key is not None:
    print (max_key)
else:
    print ('dict is empty')

