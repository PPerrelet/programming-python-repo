# Write a program named age.py that asks the user to enter their age, 
# then calculates and reports the future age 10, 20, 30, and 40 years from now.

age = int(input('How old are you ? '))
print(f'You are {age} years old')

years = 0
while years < 40:
    age += 10
    years += 10

    print(f'In {years} years, you will be {age} years old.')

# This solution reduces the repetition by calling int
# once only.

age = int(input('How old are you? '))
print()
print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')

# test