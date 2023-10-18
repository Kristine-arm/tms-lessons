# import csv
# header = ('name', 'surname', 'gender')
# person = [('Anna', 'Bana', 'female')]
# with open ('file_06.csv', 'w') as file:
#     writer = csv.writer(file, delimiter=',')
#     writer.writerow(header)
#     for human in person:
#         writer.writerow(human)

#other solution
import csv
with open ('file_06.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['name', 'surname', 'gender'])
    writer.writerow( [('Anna', 'Bana', 'female')])