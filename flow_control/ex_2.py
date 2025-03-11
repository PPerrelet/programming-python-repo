# Write a function, even_or_odd, that determines whether its argument is an even or odd number. 
# If it's even, the function should print 'even'; otherwise, it should print 'odd'. Assume the argument is always an integer.

def get_num(prompt):
    return int(input(prompt))

def even_or_odd(num):
    if num % 2 == 0:
        print('even')
    else:
        print('odd')

number = get_num('Enter your number here: ')
answer = even_or_odd(number)