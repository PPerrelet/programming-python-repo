# Without running the following code, what do you think it will do?

# This code will result in an error because the invocation on line (10) has 3 arguments.
# and the parameter on line (6) only allows for 2 arguments.

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)
