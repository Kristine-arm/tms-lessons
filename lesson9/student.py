#Создайте класс Student, с полями full_name, agerage_mark (средняя оценка).
class Student:
    def __init__(self, full_name, average_mark ):
        self.full_name = full_name
        self.average_mark = average_mark

#Добавьте в класс метод get_scholarship, который подсчитывает и возвращает стипендию данного студента по следующему алгоритму:
#Если средняя оценка < 6 - вернуть 60 (рублей)
#Если средняя оценка >= 6, но < 8 - вернуть 80 (рублей)
#Если средняя оценка >= 8 - вернуть 100 (рублей)

    def get_scholarship(self):
        if self.average_mark <6:
            return 'Give back 60 rubles'
        elif self.average_mark >= 6 and self.average_mark <8:
            return 'Give back 80 rubles'
        else:
            return 'Give back 100 rubles'

    def is_excellent(self):
        return self.average_mark >= 9


student1 = Student('Jozek', 4.65)
student2 = Student('Pawel', 6)
student3 = Student('Anna', 8)
student4 = Student('Ani', 10)

print(student1.get_scholarship())
print(student2.get_scholarship())
print(student3.get_scholarship())
print(student4.get_scholarship())

print(student1.is_excellent())
print(student2.is_excellent())
print(student3.is_excellent())
print(student4.is_excellent())