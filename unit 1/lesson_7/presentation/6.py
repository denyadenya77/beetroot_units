# Пользователь вводит список чисел через пробел, вывести новый список содержащий только четные элементы
# (с помощью списковых включений)

user = list(map(int, input('Enter:').split()))

list1 = [x for x in user if x % 2 == 0]
print(list1)