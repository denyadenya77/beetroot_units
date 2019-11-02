# Пользователь вводить возраст. Написать функцию, если возраст больше 16 то объявить внутри функции функцию
# show_available_content, которая будет показывать доступные фильмы, вызвать show_available_content которая
# показывает скрытые данные. Если возраст меньше 16, вернуть сообщение что пользователю информация недоступна.


def age_limit(a):
    def show_available_content():
        print('Let\'s watch hot movies!')
    if a >= 16:
        return show_available_content()
    else:
        print('Not today!')


user = int(input('Enter your age: '))
age_limit(user)
