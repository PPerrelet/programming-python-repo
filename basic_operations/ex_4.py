# Refactor the code from the previous exercise to use coercion to print 15 instead.

# concatenation of two digits that are actually strings due to closed quotations.
print('5' + '10') 

# Convert the strings into integers but this adds the two strings together then creates and intieger.
print(int('5' + '10'))

# Convert the two strings into integers individually and then add them together.
print(int('5') + int('10'))