import re
import cx_Oracle
import db_config
import sys


con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)
cursor = con.cursor()

cursor.execute("""INSERT INTO email.email ("EnronEmailFrm", "Subject") VALUES ('raj.kr79@gmail.com', 'test')""")
cursor.execute("COMMIT")