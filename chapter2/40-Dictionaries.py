'''
1. Create a dictionaries with curly bracket {}
2. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type;
strings and numbers can always be keys.
3. Cannot have multiple keys, each key should be unique
4. Tuples can be used as keys if they contain only strings, numbers, or tuples;
if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.
5. You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().
6. The main operations on a dictionary are storing a value with some key and extracting the value given the key.
7. It is also possible to delete a key:value pair with del.
8. If you store using a key that is already in use, the old value associated with that key is forgotten.
9. It is an error to extract a value using a non-existent key.
10. Performing list(d.keys()) on a dictionary returns a list of all the keys used in the dictionary, in arbitrary order
(if you want it sorted, just use sorted(d.keys()) instead).
11. To check whether a single key is in the dictionary, use the in keyword.
'''
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