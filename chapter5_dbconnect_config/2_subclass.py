import cx_Oracle
import db_config

class MyConnection(cx_Oracle.Connection):

    def __init__(self):
        #print("Connecting to database")
        return super(MyConnection, self).__init__(db_config.user, db_config.pw, db_config.dsn)

con = MyConnection()
cur = con.cursor()

cur.execute("select count(*) from HR.EMPLOYEES where DEPARTMENT_ID =50")
count, = cur.fetchone()
print(count)
#print("Number of rows:", count)