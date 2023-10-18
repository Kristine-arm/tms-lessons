import openpyxl

wb= openpyxl.Workbook()
sheet=wb.active
sheet['A1']='name'
sheet['B1']='surname'
sheet['A2']='Kristine'
sheet['B2']='Sargsyants'

wb.save('file_09.xlsx')
