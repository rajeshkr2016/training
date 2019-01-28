tel = {'jack': 4098, 'sape': 4139}

tel['guido'] = 4127
print(tel)

print(tel['jack'])

keyList=list(tel.keys())
print(keyList)

sortedkeyList= sorted(tel.keys())
print(sortedkeyList)

if 'guido' in tel:
    print(tel['guido'])

if 'jack' not in tel:
    print("Key jack now in the dict")

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
dict1= dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict1)

# dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
newDickt1= {x: x**2 for x in (2, 4, 6)}
print(newDickt1)

newDickt2= dict(sape=4139, guido=4127, jack=4098)
print(newDickt2)
