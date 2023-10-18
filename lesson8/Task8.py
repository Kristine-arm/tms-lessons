import csv
with open ('file_07.csv', 'r') as file:
    reader = csv.reader(file)
    index=0
    for row in reader:
        if index==1:
            print(row)
        index+=1
