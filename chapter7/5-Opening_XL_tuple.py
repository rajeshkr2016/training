import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Demo_Sheet1']
#tuple(sheet['A1':'C3'])

for rowOfCellObjects in sheet['A1':'C10']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')