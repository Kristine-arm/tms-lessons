import csv

name=input('write the name   ')
surname=input('write the surname   ')
age=input('write the age   ')

with open('file_07.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['name', 'surname', 'age'])
    writer.writerow([name, surname, age])