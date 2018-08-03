# https://docs.python.org/3/library/re.html

import re

#fname="/Users/srramar/Downloads/AdminServer-diagnostic.log"

#logfile = open("AdminServer-diagnostic.log", "r")

for line in open("AdminServer-diagnostic.log", "r"):
    if re.match("(.*)ERROR(.*)", line) and re.match("(.*)2018(.*)", line)  :
        print(line)
