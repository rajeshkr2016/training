'''
It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”);
however, lists are not efficient for this purpose.
While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow
(because all of the other elements have to be shifted by one).
'''

import os
from collections import deque


queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives

queue.popleft()                 # The first to arrive now leaves
#print(queue)

queue.popleft()
#print(queue)



import sys



print (type(sys.path))

for path in sys.path:
    print(path)