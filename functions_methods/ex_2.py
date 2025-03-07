# Take a look at this code snippet:

foo = 'bar' # global

def set_foo():
    # local
    foo = 'qux'
    return foo

set_foo()
print(foo)

# What does this program print? Why?
# This program will print 'bar'.
# This is because out print function is passing'foo' which is part of our global scope 