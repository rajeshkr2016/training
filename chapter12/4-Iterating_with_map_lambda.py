dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
output=list(map(lambda x : x['name'], dict_a))
print(output)


output1=list(map(lambda x : x['points']*10,  dict_a))
print(output1)


output2=list(map(lambda x : x['name'] == "python", dict_a))
print(output2)


list_a = [1, 2, 3]
list_b = [10, 20, 30]
  
output3=set(map(lambda x, y: x + y, list_a, list_b))
print(output3)
