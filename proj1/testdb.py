import re
import cx_Oracle
import db_config
import sys


con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)
cursor = con.cursor()

sql = """INSERT INTO email.email ("EnronEmailFrm", "Subject") VALUES (:EnronEmailFrm, :subject)"""

#cursor.execute("""INSERT INTO email.email ("EnronEmailFrm", "Subject") VALUES ('raj.kr79@gmail.com', 'test')"""
# (:EnronEmailFrm,:subject)""")

try:
  cursor.prepare(sql)
except cx_Oracle.DatabaseError as exception:
  print('Failed to prepare cursor')
  print(exception)
  exit (1)

try:
  cursor.execute(None,EnronEmailFrm="raj.kr79@gmail.com", subject="testSecond")
  print(cursor.bindnames())
  print("Rows inserted successfully")
except cx_Oracle.DatabaseError as exception:
  print('Failed to insert row')
  print(exception)
  exit (1)
con.commit