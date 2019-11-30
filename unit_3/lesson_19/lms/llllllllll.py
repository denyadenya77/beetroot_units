import os
from datetime import datetime

# print(os.getcwd())  # get current working directory

os.chdir('/home/denis/PycharmProjects/beetroot_academy/unit_3/lesson_19')  # change current working directory
# print(os.getcwd())
#
# print(os.listdir())  # list of files/derectories in current working directory

# os.mkdir('lms-2')  # создать директорию
# os.makedirs('lms-2/myfiles') # создать вложенные директории

# os.rmdir()  # удалить директорию
# os.removedirs()  # удалить вложенную директорию

# os.rename('file.txt', 'new_file_name.txt')  # переименование файлов

# print(os.stat('lms/test.txt').st_size) # file info
# mod_time = os.stat('lms/test.txt').st_mtime # file info. last modification time
# print(datetime.fromtimestamp(mod_time))  # time in human format


for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print(f'Current path: {dirpath}.')
    print(f'Directories: {dirnames}.')
    print(f'Files: {filenames}.')
    print()

# print(os.environ.get('HOME'))  # environment variables

# file_path = os.path.join(os.environ.get("HOME"), 'test_2.txt')
# with open(file_path, 'w') as f:
#     f.write('')


# print(os.path.basename('/fake_path/fake_file.txt'))
# print(os.path.dirname('/fake_path/fake_file.txt'))
# print(os.path.split('/fake_path/fake_file.txt'))
# print(os.path.exists('/fake_path/fake_file.txt'))  # False if fake

# print(os.path.splitext('/fake_path/fake_file.txt'))  # ('/fake_path/fake_file', '.txt')


print(os.cpu_count())

