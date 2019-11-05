# Create a generator function that yields all squares of integers within a given range, i.e., arguments start and stop.


def my_generator(start, stop):
    num = start
    while num < stop:
        square_num = num ** 2
        yield square_num
        num +=1


a = my_generator(1, 10)

for x in a:
    print(x)
