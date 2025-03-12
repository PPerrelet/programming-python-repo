# Consider the data in the following table:

# Alice	    USA
# Francois	Canada
# Inti	    Peru
# Monika	Germany
# Sanyu	    Uganda
# Yoshitaka	Japan

# You need to write some Python code to determine the country name associated with one of the listed names. 
# Your code should include the data structure(s) you need and at least one test case to ensure the code works.

country = {
    'Alice':        'USA',
    'Francois':     'Canada',
    'Inti':         'Peru',
    'Monika':       'Germany',
    'Sanyu':        'Uganda',
    'Yoshitaka':    'Japan',
}

print('Enter one of the following names: Alice, Francois, Inti, Monika, Sanyu, Yoshitaka.')
name = input()  # Capture the input correctly
print(f"{name} lives in {country[name]}")