# Without running the following code, what do you think it will do?

# This code will print 42, 3.141592, 2.718 
# Since we passed the arguments on line 11 we replaced the default values within our parameters on line 6.

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)