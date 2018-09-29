import openpyxl
wb = openpyxl.load_workbook('example.xlsx')

# https://openpyxl.readthedocs.io/en/stable/

#check the type of wb
print(type(wb))
#get all the sheets from xlxs file
sheets = wb.sheetnames
print("All sheets from the excel:", sheets)

sheet1 = wb["Demo_Sheet1"]
print(str(sheet1["A1"].value)+ " - "+ sheet1["B1"].value +" - "+str(sheet1["C1"].value))

