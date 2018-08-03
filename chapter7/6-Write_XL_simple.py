import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
#sheet.title = 'Sample Sheet'
wb.create_sheet(index=0, title='First Sheet')
wb.save('example_new1.xlsx')