#Создайте класс Person. У класса должно быть три поля: full_name, age, gender, которые должны заполняться в конструкторе. Будем считать что поле gender имеет тип str и может быть либо 'M' (male), либо 'F' (female).
import datetime
class Person:
    def __init__(self, full_name, age, gender):
        self.full_name = full_name
        self.age = age
        self.gender = gender

    def print_person_info(self):
        print(f"Person: {self.full_name} {self.gender}, {self.age} years old")

    #Добавьте метод get_birth_year, которая возвращает год рождения человека (рассчитанное как 2023 - age)

    def get_birth_year(self):
        return (f'{2023 - self.age}')
 #Замените цифру 2023 на текущий год (чтобы ваша программа работала правильно даже через год). Текущий год можно взять с помощью модуля datetime
    def get_birth_year_now(self):
        current_time = datetime.datetime.now()
        return current_time.year - self.age

p = Person('Ivan Ivanov', 20, 'Male')

print(p.full_name)
print(p.age)
print(p.gender)
print(p.get_birth_year())
print(p.get_birth_year_now())