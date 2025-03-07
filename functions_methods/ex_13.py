# Without running the following code, what do you think it will do?
# Will result in error because default values must be placed at the end of parameter.
# You must follow default parameters with other default parameters.

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)