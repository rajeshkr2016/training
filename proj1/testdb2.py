import re
import psycopg2
#import db_config1
import sys


con = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='mysecretpassword'")
cursor = con.cursor()

#sql = """INSERT INTO email.email ("EnronEmailFrm", "Subject") (%(first_name)s, %(last_name)s)"""

#cursor.execute("""INSERT INTO email.email ("EnronEmailFrm", "Subject") VALUES ('raj.kr79@gmail.com', 'test')"""
# (:EnronEmailFrm,:subject)""")

# try:
#   cursor.prepare(sql)
# except cx_Oracle.DatabaseError as exception:
#   print('Failed to prepare cursor')
#   print(exception)
#   exit (1)
rows = {}
rows={0: "raj.kr79@gmail.com", 1: "testSecond"}

try:
  cursor.executemany("""INSERT INTO email.email (EnronEmailFrm, Subject) (%(EnronEmailFrm)s, %(Subject)s)""",rows)

  #print(cursor.bindnames())
  print("Rows inserted successfully")
except Exception as exception:
  print('Failed to insert row')
  print(exception)
  exit (1)
con.commit