#import dbconnect
import re

import json
import logging
from pythonjsonlogger import jsonlogger

original_errmsg= json.decoder.errmsg

def our_errmsg(msg, doc, pos, end=None):
    json.last_error_position= json.decoder.linecol(doc, pos)
    return original_errmsg(msg, doc, pos, end)


with open("enron-emails.json") as fh:
    for flines in fh.readlines():
            #flines1=re.sub('\n',',',flines)
            #print(flines)
            try:
                emailjdata=json.load(flines)
                print(emailjdata)
            except ValueError as e:
                print("error at", json.last_error_position)
                continue

