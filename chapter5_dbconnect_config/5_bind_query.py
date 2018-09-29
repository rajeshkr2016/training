import cx_Oracle
import db_config

newSalAdd= 10
def querydb():
    cur.prepare("select Employee_id, First_Name, Last_Name, SALARY from HR.EMPLOYEES where DEPARTMENT_ID =:id")

    cur.execute(None, id=100)
    res = cur.fetchall()
    print(res)
    #unwrapResults(res)
    converToDict(res)

def unwrapResults(res):
    for item in res:
        print(item)
        for items in item:
            if items == "Daniel":
                newSal=item[3]*newSalAdd
                print(items, "New Sal =", newSal)


def converToDict(res):
    resList=[]
    resDict={}
    for item in res:
        print(item[0],item[1])
        resDict["id"]=item[0]
        resDict["first name"] = item[1]
        resDict["last name"] = item[2]
        resDict["salary"] = item[3]
        resList.append(resDict.copy())
    print(resList)



try:
    con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)
    cur = con.cursor()
    result= querydb()

except:
    print("Not abel to conenct")







'''
for rows in res:
    print(rows)
    for item in rows:
        print(item)
'''