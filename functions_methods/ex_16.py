# In the code shown below, identify all of the function names and parameters present in the code. 
# Include the line numbers for each item identified.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# built in function names
# float line 8
# input line 8
# pint line 13

# function names 
# multiply line 4, 12
# get_num line 7, 10, 11

# parameters
# left line 4, 5
# right line 4, 5
# prompt line 7, 8