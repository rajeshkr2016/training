import re
#from time import datetime
import datetime

with open('somefile.txt', 'a') as the_file:
    date=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    the_file.write(date+'\n')
    the_file.write("write complete"+'\n')