# Write a program named age.py that includes someone's age 
# and then calculates and reports the future age 10, 20, 30, and 40 years from now.

age = int(input()) # Collecting age

print(f'You are {age} years old.') # print age

loop_num = 10  # starting age forecast 
while loop_num <= 40: # stop calculating at 40 years
    print(f'In {loop_num} years, you will be {loop_num + age} years old.')
    loop_num = loop_num + 10 # calculate in increments of 10
    

