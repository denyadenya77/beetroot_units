# Пользователь вводит список чисел через пробел, вывести новый список в котором элементы из введенного
# пользователем списка будут умножены на 2 с помощью списковых включений.

user = list(map(int, input('Enter: ').split()))
print(user)

list1 = [x * 2 for x in user]
print(list1)
