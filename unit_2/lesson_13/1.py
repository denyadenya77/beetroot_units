# Create a function that takes in 2 numbers and a mathematical function, that also takes 2 numbers as arguments,
# and then returns the result of the passed argument function given the 2 numbers.

def sum_1(a, b):
    return a + b

def func_1(a, b, c):
    return c(a, b)

print(func_1(4, 4, sum_1))


# или так:

def func_2(a, b):
    def sum_2():
        return a + b
    return sum_2()

print(func_2(5, 5))

# или даже так:

def func_3(a, b):
    def sum_3():
        return a + b
    return sum_3


call_the_result = func_3(10, 10)
print(call_the_result())
