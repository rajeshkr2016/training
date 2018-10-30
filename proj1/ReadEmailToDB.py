import re
import cx_Oracle
import db_config
import sys
import json
import logging
from pythonjsonlogger import jsonlogger

try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)

cur = con.cursor()
cur1 = con.cursor()

emailDict=[]
with open("enron-emails.json") as fh:
    for line in fh:
        emailDict.append(json.loads(line))


    rows=[]

    # cur.execute("select * from email.email")
    # for row in cur.fetchall():
    #     print(row)
    tup=tuple()
    for i in range(len(emailDict)-1):
        # try:
        try:
            tup=(emailDict[i]["from"], emailDict[i]["subject"])
            #print(tup)
            rows.append(tup)
            #print(rows)
            #cur.prepare("INSERT INTO EMAIL.EMAIL(EnronEmailFrm,subject) VALUES (:from, :subject)")
            #print(cur.bindnames())
            # except Exception as e:
            #     print("Exception:",e)
            #     continue
            # print(type(rows))
        except Exception as e:
            print("Exception for line no:"+str(i)+":",e)
            continue
    print("Rows:" + str(rows))
    cur.executemany("INSERT INTO EMAIL.EMAIL(EnronEmailFrm,subject) VALUES (:from, :subject)", rows)

        #cur.execute("""INSERT INTO EMAIL.EMAIL (\"EnronEmailFrm\",\"subject\") VALUES (%s, %s)""",rows)

        #cur.prepare("INSERT INTO python_modules(module_name, file_path) VALUES (:1, :2)")
con.commit()

