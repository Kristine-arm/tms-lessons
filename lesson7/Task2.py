#Пользователь вводит произвольное количество маленьких латинских букв через пробел.
#Напишите функцию remove_vowels, которая принимает список из этих букв и удаляет из него все гласные буквы.
#Выведите результат работы на экран.

# def vowel():
#     s=input('write small letters with space   ').split()
#     x = s.copy()
#     for i in s:
#         if i in  ['a', 'e', 'i', 'o', 'u']:
#             x.remove(i)
#     return x

def vowel():
    s = input('write small letters with space   ').split()
    x = []
    for i in s:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            x.append(i)
    return x

print(vowel())

#with filter
def vowel (l: list[str]) -> list[str]:
    return list(filter(lambda x: x not in ['a', 'e', 'i', 'o', 'u'], l))

user = input("Enter lowercase letters separated by space: ").split()
print(vowel(user))




