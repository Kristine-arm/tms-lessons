from person import Person

# Создайте объекты класса Person для ваших вымышленных друзей
friend1 = Person('Anna Novak', 25, 'F')
friend2 = Person('Ani Many', 30, 'F')
friend3 = Person('Borat Sagdiev', 56, 'M')
friend4 = Person('Zordon', 96, 'M')
friend5 = Person('Kaczynski', 99, 'F')

my_friends = [friend1, friend2, friend3, friend4, friend5]

#Выведите информацию о каждом друге на экран.

friend1.print_person_info()
friend2.print_person_info()
friend3.print_person_info()

#or i could use for loop
#for friend in my_friends:
    #friend.print_person_info()

#Найдите среди друзей самого старшего, выведите информацию о нём на экран.
oldest_friend = max(my_friends, key=lambda friend: friend.age)

print('The oldest friend is: ', end='')
oldest_friend.print_person_info()

#Выведите на экран информацию о всех друзьях мужского пола (можно использовать функцию filter, либо генератор списков).

male_friends = list(filter(lambda friend: friend.gender == 'M', my_friends))
for male_friend in male_friends:
    print('The male friend is: ', end='')
    male_friend.print_person_info()

#Заверните код из пунктов 5 и 6 в функции get_oldest_person и filter_male_person соответственно.

oldest_male_friend = max(my_friends, key=lambda friend: (friend.age if friend.gender == 'M' else 0))
oldest_male_friend.print_person_info()