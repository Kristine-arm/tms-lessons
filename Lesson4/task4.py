import random
hiden_number = random.randint(0, 100)

while True:
    user_number = int(input("Guess the number between 0 and 100: "))

    if user_number == hiden_number:
        print('Congrats')
        break
    elif user_number < hiden_number:
        print("wrong, number is greater")
    else:
        print("wrong, number is smaller")













