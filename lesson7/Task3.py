#Решите прошлую задачу, в которой теперь пользователь может вводить буквы в любом регистре. Вам по прежнему нужно удалить все гласные. При этом вывести результат нужно вывести сохранив изначальный регистр.
#with filter
def vowel (l: list[str]) -> list[str]:
    return list(filter(lambda x: x.lower() not in ['a', 'e', 'i', 'o', 'u'], l))

user = input("Enter lowercase letters separated by space: ").split()
print(vowel(user))

#with for loop
def vowel():
    s = input('write small letters with space   ').split()
    x = []
    for i in s:
        if i.lower() not in ['a', 'e', 'i', 'o', 'u']:
            x.append(i)
    return x

print(vowel())