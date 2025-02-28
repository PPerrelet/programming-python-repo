# To what value does the following expression evaluate?

print('foo' == 'Foo') # False because the equality operator (==) is case sensitive.

print('foo' > 'Foo')  # True because lowercase is considered greater than uppercase due to the ASCII value.

print('foo'.casefold() == 'Foo'.casefold()) # True. casefold turns the string into all lowercase. 