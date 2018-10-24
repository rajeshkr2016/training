#import dbconnect
import cx_Oracle
import db_config
import re

rows = [(1, "First" ), (2, "Second" ),
         (3, "Third" ), (4, "Fourth" ),
         (5, "Fifth" ), (6, "Sixth" ),
         (7, "Seventh" )]

con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)
print("Database version:", con.version)



cur = con.cursor()

cur.executemany("insert into email.email(From,Subject) values (%s, %s)", rows)
# Now query the results back
# cur.execute("DELETE FROM mytab")
cur.execute("commit")

# with open("enron-email.json") as fh:
#     for econtents in fh:

