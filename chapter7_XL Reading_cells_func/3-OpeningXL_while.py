import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet1 = wb["Demo_Sheet1"]

r=1
while r<11:
    print("row", r, sheet1.cell(row=r, column=2).value)
    r=r+1

