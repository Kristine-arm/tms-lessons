number = int(input('dej liczbe: '))

value = 0
while number > 9:
    decimal = number % 10
    smaller_number = number // 10
    value += decimal
    number = smaller_number

print(value+number)