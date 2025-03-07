# Without running the following code, what do you think it will do?
# This code will print 42, 3, 2.
# Since the line 10 is only passing a single argument '42'.
# The other parameters "second" and "third" will print thier default values. 
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)