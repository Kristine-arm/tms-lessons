from student import Student
#Создайте переменную students - список объектов класса Student, с разными именами и средней оценкой.

student1 = Student('Jozek', 4.65)
student2 = Student('Pawel', 6)
student3 = Student('Anna', 8)
student4 = Student('Ani', 10)

students = [student1, student2, student3, student4]
#Посчитайте суммарную стипендию для всех студентов.

calc_sum_scholarship = sum(map(lambda student: student.average_mark, students))
#or I could use list generator: calc_sum_scholarship= sum(student.get_scholarship() for student in students)
print('sum is', calc_sum_scholarship)

#Посчитайте количество отличников (используйте метод is_excellent).
count_excellent = 0
for student in students:
    if student.is_excellent():
        count_excellent += 1

#with list generator : count_excellent = sum(1 for student in students if student.is_excellent())

print('Number of excellent students:', count_excellent)

#Заверните код для пунктов 4 и 5 к функции calc_sum_scholarship и get_excellent_student_count
#calculate the sum of excellent students

def razem(students):

    calc_x = sum(map(lambda student: student.average_mark, students))
    excellent_count = sum(1 for student in students if student.is_excellent())
    return excellent_count, calc_x

print(razem(students))