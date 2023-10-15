#Дан список чисел. Удалите из него отрицательные числа.
def input_list():
    result = str(filter(lambda x: int(x) >0, input('Wpisz liczby rozdzielane spacja   ').split()))
    return result

print(input_list())

#with generator of list
def input_list():
    return [int(x) for x in input().split() if x>0]

my_list = input_list()
print(my_list)

#with list generator
def input_list():
    positive_numbers= [int(x) for x in input('Wpisz liczby  ').split() if int(x)>0]
    return positive_numbers

result = input_list()
print(result)

#with for loop
def input_list():
    positive_numbers=[]
    for x in input('Wpisz liczby  ').split():
        if int(x)>0:
            positive_numbers.append(int(x))
    return positive_numbers

result = input_list()
print(result)

#Дан список чисел. Удалите из него нечётные числа.
def input_list():
    result = list(filter(lambda x: int(x)%2==0, input('Wpisz liczby rozdzielane spacja   ').split()))
    return result

print(input_list())

#with list generator
def input_list():
    return [int(x) for x in input().split() if int(x)%2==0]

my_list = input_list()
print(my_list)

#with for loop
def input_list():
    even_numbers=[]
    for x in input().split():
        if int(x)%2==0:
            even_numbers.append(int(x))
    return even_numbers

my_list = input_list()
print(my_list)


#Дан список чисел. Выведите три числа: количество положительных чисел, поличество нулей, и количество отрицательных чисел. Используйте функции filter и len.
def input_list():
    numbers = [int(x) for x in input('Wpisz liczby rozdzielane spacja: ').split()]
    positive_count = len(list(filter(lambda x: int(x)>0, numbers )))
    zero_count=  len(list(filter(lambda x: int(x)==0, numbers)))
    negative_count= len(list(filter(lambda x: int(x)<0, numbers)))
    return positive_count, zero_count, negative_count

positive_count, zero_count, negative_count = input_list()

print(positive_count)
print(zero_count)
print(negative_count)

#Напишите свою реализацию функций my_filter, возвращающую список.
#find common values from 2 lists
def input_list():
    a=input('Wpisz liczby rozdzielane spacja   ')
    b=input('Wpisz liczby rozdzielane spacja  jeszce  ')
    result = list(filter(lambda x: x in a.split(),b.split()))

    return result

print(input_list())

#with for loop and generator lista
def input_list():
    a = input('Wpisz liczby rozdzielane spacją: ')
    b = input('Wpisz liczby rozdzielane spacją jeszcze raz: ')

    # Split the input strings into lists of numbers
    list_a = a.split()
    list_b = b.split()

    # Convert the list elements to integers
    list_a = [int(x) for x in list_a]
    list_b = [int(x) for x in list_b]

    common_elements = []

    # Use nested for loops to compare elements from both lists
    for num_a in list_a:
        for num_b in list_b:
            if num_a == num_b:
                common_elements.append(num_a)

    # Print the common elements
    if common_elements:
        print("Common elements:", common_elements)
    else:
        print("No common elements found.")

# Call the function
input_list()

#or a but other way
def input_list():
    # Get input from the user and split it into lists of numbers
    list_a = input('Enter numbers separated by spaces: ').split()
    list_b = input('Enter more numbers separated by spaces: ').split()

    # Convert the lists of strings to lists of integers
    list_a = [int(x) for x in list_a]
    list_b = [int(x) for x in list_b]

    # Find the common elements using set intersection
    common_elements = set(list_a) & set(list_b)

    # Print the common elements
    if common_elements:
        print("Common elements:", list(common_elements))
    else:
        print("No common elements found.")

# Call the function
input_list()

