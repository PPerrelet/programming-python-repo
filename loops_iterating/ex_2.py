# Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter. 
# The updated code should use a for loop to display the future ages.

# Write a program named age.py that asks the user to enter their age,
# then calculates and reports the future age 10, 20, 30, and 40 years from now.

age = int(input('How old are you ? '))
print(f'You are {age} years old')

years = []  

for x in range(1, 5):
    year_ten = x * 10
    years.append(year_ten) 
    print(f'In {year_ten} years, you will be {age + year_ten} years old.')


age = int(input('How old are you? '))
print(f'You are {age} years old.')
print()

for future in range(10, 50, 10):
    print(f'In {future} years, you will be '
          f'{age + future} years old.')