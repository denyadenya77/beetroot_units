# Create a function decorator that prints the name of the current running
# function by using the __name__ attribute. Make sure to also decorate some
# different functions to see that it works properly.

from functools import reduce


def current_function(f):
    def wrapper(*args):
        print(f'Function {f.__name__} is working!')
    return wrapper


@current_function
def the_sum(x, y):
    return x + y


@current_function
def perimeter(*args):
    return reduce(lambda x, y: x + y, args)


a = the_sum(3, 7)
b = perimeter(1, 2, 3)
