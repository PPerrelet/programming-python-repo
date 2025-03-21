# Without running this code, what will it print? Why?
dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1) # dict constructor creates a shallow copy for dict2
dict2['Monty Python'] = 'Holy Grail' # modify dict 2 shallow copy

print(dict1['Monty Python']) # dict1 still prints 'Life of Brian'
print(dict2['Monty Python']) # dict2 has been changed to 'Holy Grail'
print(dict1['Monty Python'] == dict2['Monty Python'])
print(dict1['Monty Python'] is dict2['Monty Python'])
print(dict1)
print(dict2)