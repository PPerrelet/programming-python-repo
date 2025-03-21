# Without running this code, what will it print? Why?

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1) # shallow copy share nests
dict1['a'][1] = 42 # modify dict1 nest
dict1['a'] = 0
print(dict2['a']) # dict2 will print 'a' : [1, 42, 3]
print(dict1['a']) # so will dict1
print(dict1['a'] is dict2['a'])