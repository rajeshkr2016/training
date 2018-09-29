import openpyxl
wb = openpyxl.load_workbook('example.xlsx')


sheet1 = wb["Demo_Sheet1"]

def getXlValue(r,c):
    return sheet1.cell(row=r, column=c).value

r=1
while True:
    if (getXlValue(r, 1)):
        c = 1
        print("* Starting row :",r,"*")
        while True:
            if (getXlValue(r, c)):
                print(getXlValue(r, c))
                c = c + 1
            else:
                print("end of columns @ row no:", r)
                break
    else:
        print("*** end of all rows ***")
        break
    r = r + 1
