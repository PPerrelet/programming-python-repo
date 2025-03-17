pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
values = pets.values()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)
print(values)

# Without running the following code, what values will be printed by line 10?

# ['Cat', 'Bird', 'Snake']