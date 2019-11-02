# Объявить словарь, в котором ключом будет permission (admin, loggedin, unknown etc) а значениями будут ссылки на
# функции, которые отображают доступный функционал данного пользователя. Объявить класс Person, у которого есть
# атрибут (свойство) permission. Создать экземпляры класса Person с различными permission и отобразить доступный
# функционал по словарю.


# Способ первый: как по заданию.

def create_content():
    print('The content is created!')


def delete_content():
    print('The content is deleted!')


def send_message():
    print('Message has been sent!')


def create_comment():
    print('Comment was created!')


def create_account():
    print('Account was created!')


permissions = {'admin': {'create_content': create_content, 'delete_content': delete_content},
              'loggedin': {'send_message': send_message, 'create_comment': create_comment},
              'unknown': {'create_account': create_account}}


class Person:

    def __init__(self, permission):
        self.permission = permission


admin_1 = Person(permissions['admin'])
loggedin_1 = Person(permissions['loggedin'])
unknown_1 = Person(permissions['unknown'])

admin_1.permission['create_content']()
loggedin_1.permission['send_message']()
unknown_1.permission['create_account']()
