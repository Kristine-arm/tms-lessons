from person import Person

# Создайте переменную my_best_friend класса Person
my_best_friend = Person('Ivan Ivanov', 20, 'M')

# Выведите информацию my_best_friend на экран (метод print_person_info)
my_best_friend.print_person_info()

# Выведите год рождения my_best_friend на экран
birth_year = my_best_friend.get_birth_year()
print(f"Birth Year: {birth_year}")