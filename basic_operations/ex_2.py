# This question may be a little challenging if your math skills are rusty.
#  Don't be afraid to take advantage of the hints. Try your best to solve the
#  problem, but don't feel compelled to complete it if you become frustrated.

# Use the REPL and the arithmetic operators to extract the individual digits of 4936:

# One place is 6.
# Tens place is 3.
# Hundreds place is 9.
# Thousands place is 4.

# Each digit may require multiple Python statements.

number = 4936

ones = number % 10
tens = ((number // 10) % 10)
hundreds = (((number // 10) // 10) % 10)
thousands = ((((number // 10) // 10) // 10) % 10)

print(ones)
print(tens)
print(hundreds)
print(thousands)

# or 

num = 4936

one_s = num % 10

num = num // 10
ten_s = num % 10

num = num // 10
hundred_s = num % 10

num = num // 10
thousand_s = num % 10 

print(one_s)
print(ten_s)
print(hundred_s)
print(thousand_s)

# as a loop

loop_num = 4936 
while loop_num > 0:
    print(loop_num % 10)
    loop_num = loop_num // 10
    