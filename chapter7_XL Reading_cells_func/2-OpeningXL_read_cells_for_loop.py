import openpyxl
wb = openpyxl.load_workbook('example.xlsx')

#read sheet1
sheet1 = wb["Demo_Sheet1"]

#print(len(sheet1))
for i in range(1, 11, 1):
        print(i, sheet1.cell(row=i, column=2).value)

