# Without running the following code, what do you think it will do?
# This code will print 42, 3.141592, 2.
# The argument on line 12 will place the first parameter on line 7 with 42.
# The argument one line 12 will the the second parameter on line 7 with 3.141592.
# Since there is no third argument passed on line 12 it will default to 2 as seen on line 7.

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)