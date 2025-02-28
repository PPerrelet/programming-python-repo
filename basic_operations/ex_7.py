# What will the following code do? Why?

int('3.1415')

# Will result in an error because we are attempting to push a string that converts to float through the int function.
# The int function can only convert strings that represent whole numbers

number = float('3.1415') # convert the number to float
print(number) # our stored float
print(int(number)) # convert the float to int
