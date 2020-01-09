# Создать файл server.py который будет слушать подключения от клиента, получать сообщение и отправлять его обратно
# тому же клиенту.


import socket

host = socket.gethostbyname(socket.gethostname())
port = 9090

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

quit_server = False
print('Server started.')

while not quit_server:
    try:
        data, addr = s.recvfrom(1024)
        s.sendto(data, addr)
    except:
        print('\nServer stopped.')
        quit_server = True

s.close()
