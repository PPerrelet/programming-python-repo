# What does the following function do? Be sure to identify the output value.

def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))

# Line 4 will sort the dictionary keys in descending order. sorted
# It will then take key #1 of that of that sorted dictionary.   dictionary.keys())[1]
# Last it will capitalize that key and print it out to us. .upper()