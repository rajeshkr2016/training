import cx_Oracle
import db_config
import re

con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)
print("Database version:", con.version)

cur = con.cursor()
cur.execute("select count(*) from email.email")
res, = cur.fetchall()#.strip(',')
res2=str(res)
res3=re.sub(',|\)|\(','',res2)

#con.close()
print(res3)

con.close()