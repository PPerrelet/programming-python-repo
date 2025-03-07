# Write a program that uses a multiply function to multiply two numbers and returns the result.
# Ask the user to enter the two numbers, then output the numbers and result as a simple equation.

def get_number(prompt):
    number = input(prompt)
    return float(number)

first_number = get_number('Enter first number: ')
second_number = get_number('Enter second number: ')

def multiply(left, right):
    return left * right

product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')
