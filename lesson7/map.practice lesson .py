#Напишите функцию input_list, которая не принимает входных аргументов, в просто читает строку, которую ввёл пользователь (вызывая функцию input), разбивает её по пробелам (с помощью функции split), и возвращает список целых чисел.
def input_list():
    return list(map(int, input().split()))

#OR other way
    return[int(x) for x in input().split()]

my_list = input_list()
print(my_list)

#Дан список чисел. Увеличьте каждый элемент в 100 раз.
#with lambda
def real_input_list():
    result = list(map(lambda x : int(x) * 100, input('Wpisz liczby rozdzielane spacja   ').split()))
    return result

print(real_input_list())


#with generator lista
def real_input_list():
    result = ([int(i)*100 for i in input('Wpisz liczby rozdzielane spacja   ').split()])
    print (result)

real_input_list()

#with for loop
def real_input_list():
    a = []
    for i in input('Wpisz liczby rozdzielane spacja   ').split():
        result = int(i)*100
        a.append(result)
    return a

print (real_input_list())


#Дан список чисел. Преобразуйте этот список в список строк

def real_input_list():
    result = list(map(lambda x : str(int(x) * 100), input('Wpisz liczby rozdzielane spacja   ').split()))
    return result

print(real_input_list())

#with generator lista

def real_input_list():
    result = ([str(int(i)*100) for i in input('Wpisz liczby rozdzielane spacja   ').split()])
    print (result)

real_input_list()

#with for loop
def real_input_list():
    a = []
    for i in input('Wpisz liczby rozdzielane spacja   ').split():
        result = str(int(i)*100)
        a.append(result)
    return a

print (real_input_list())

#Дан список чисел. Разделите каждый элемент на 100 и округлите до целого числа (функция round).

def real_input_list():
    result = list(map(lambda x: round(int(x)/100), input('Wpisz liczby rozdzielane spacja   ').split()))
    return result

print(real_input_list())

#with generator lista
def real_input_list():
    result = ([round(int(i)/100) for i in input('Wpisz liczby rozdzielane spacja   ').split()])
    print (result)

real_input_list()


#with for loop
def real_input_list():
    a = []
    for i in input('Wpisz liczby rozdzielane spacja   ').split():
        result = round(int(i)/100)
        a.append(result)
    return a

print (real_input_list())


#Напишите свою реализацию функций my_map, возвращающую список.
#square
def real_input_list():
    result = list(map(lambda x: int(x)**2, input('Wpisz liczby rozdzielane spacja   ').split()))
    return result

print (real_input_list())

#with list gnerator
def real_input_list():
    result = ([str(int(i) **2) for i in input('Wpisz liczby rozdzielane spacja   ').split()])
    print(result)

#with for loop
def real_input_list():
    result = []
    for i in input('Wpisz liczby rozdzielane spacja   ').split():
       result.append (int(i) ** 2)
    return result

zmienna = real_input_list()

print(zmienna)

