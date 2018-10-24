#import dbconnect
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
    # cur.bindarraysize = 7
    # cur.setinputsizes(int, 120)

    # cur1.execute("select * from email.email")
    # for row in cur1.fetchall():
    #      print(row)
    cur.execute("select * from email.email  WHERE \"EnronEmailFrm\" like '%test%'")
    for row in cur.fetchall():
        print(row)

    #try:
    for i in range(len(emailDict)-1):
        #print("position:",i)
        #print("email:", type(emailDict[i]["from"]))

        #try:
        rows = [emailDict[i]["from"], emailDict[i]["subject"]]
        # print("rows:", str(rows), "datatypes:",type(emailDict[i]["from"]),type(emailDict[i]["subject"]))
        print("Rows:"+str(rows))
        # print(type(rows))

        #cur.executemany("insert into email.email values (%s,%s)",rows)
        #sqlstr='INSERT INTO EMAIL.EMAIL(from,subject) VALUES(:frm, subject)'
        # frm="test1234"
        # subj="1234"
        cur.execute("""INSERT INTO EMAIL.EMAIL (\"EnronEmailFrm\",\"subject\") VALUES (\"%s\", \"%s\")""",rows)


        #cur.execute(""
        #cur.executemany(None, rows)
#        except Exception as ex:
#            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
#            message = template.format(type(ex).__name__, ex.args)
#            print(message)
#            continue
    #cur.execute("commit")
    # except Exception as e:
    #     print("Exception occured:",e)


    #print(emailDict)
    #print(type(emailDict[0]))

    #print(emailDict[-1])
    #print(len(emailDict))

    #print(fh.readlines())
    # emailDict=json.load(fh)
    # print(type(emailDict))
    # print("Email:",str(emailDict))
    #for flines in fh.readlines():
        #emailDict = flines.split
        #flines=re.sub('\n',',',flines)
        #print(flines)

    '''

    try:
        emailjdata=json.load(flines)
        print(emailjdata)
    except JSONDecodeError:
        print("JSON parse error")
        continue
    '''

