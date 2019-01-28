# v=sentence="We are learning python"
#
# #extracting string
# print(sentence[0:2])
# print(sentence[:2])
# print(sentence[7:15])
#
# print(sentence[::-1])
#



from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives

queue.popleft()                 # The first to arrive now leaves
print(queue)

queue.popleft()
print(queue)


