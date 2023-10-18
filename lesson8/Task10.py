import openpyxl

name=input('write the name   ')
surname=input('write the surname   ')


wb= openpyxl.Workbook()
sheet=wb.active
sheet['A1']='name'
sheet['B1']='surname'
sheet['A2']=name
sheet['B2']=surname

wb.save('file_10.xlsx')