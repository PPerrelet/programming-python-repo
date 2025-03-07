# Without running the following code, what do you think it will do?
# This will result in an error because 'first' has no default of argument.
# The 'second' and 'third' parameters have default but 'first' does not.

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()