for num in range(101):
    print(num)
    answear = input("Should we break?  ")

    if answear.lower() == "yes":
        break
    elif answear.lower() == "no":
        continue

    while answear not in ('yes','no'):
        print('Dont understand you')
        answear = input("Should we break?  ")

