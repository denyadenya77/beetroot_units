# Написать генератор для чисел Фибоначчи.

def generate_fib(exit_index):
  num_1 = 0
  num_2 = 1
  i = 0
  while i < exit_index:
    new_num = num_1 + num_2
    yield new_num
    num_1, num_2 = num_2, new_num

a = generate_fib(14)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))