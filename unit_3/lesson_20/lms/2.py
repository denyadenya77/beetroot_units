# Make a function that takes an integer (in decimal form) and convert it to a binary form using recursion.


def find(decimal_number):
    if decimal_number == 0:
        return 0
    else:
        return decimal_number % 2 + 10 * find(int(decimal_number / 2))


decimal_number = 10
print(find(decimal_number))
