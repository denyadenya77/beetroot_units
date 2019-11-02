
# Способ второй: реализация удобного вызова функции - без обращения к словарю по ключу.

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
        for k, v in permission.items():
            setattr(self, k, v)


admin_1 = Person(permissions['admin'])
loggedin_1 = Person(permissions['loggedin'])
unknown_1 = Person(permissions['unknown'])

admin_1.create_content()
loggedin_1.send_message()
unknown_1.create_account()
