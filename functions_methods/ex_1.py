# What happens when you run the following program? Why do we get that result?

# foo is only available within the function. 

# Global scope
def set_foo():
    # Local scope
    foo = 'bar'
    print(foo)

set_foo()
print(foo)