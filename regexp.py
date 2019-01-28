#!/usr/bin/env python

import re
f="1.txt"

with open(f) as fh:
    for no,line in enumerate(fh):
        if re.match("00",line):
            print("Found 00 at line No:",str(no)+" Line:" + line)