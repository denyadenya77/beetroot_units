# Создать файл client.py который будет подключаться к серверу и отправлять ему сообщения введенные
# пользователем из консоли.

import socket
import threading
import time

key = 8194

shutdown = False

def receiving(neme, sock):
    while not shutdown:
        while True:
            data, addr = sock.recvfrom(1024)
            print(data.decode('utf-8'))
            time.sleep(0.2)


host = socket.gethostbyname(socket.gethostname())
port = 0

server = ('127.0.1.1', 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(True)

t = threading.Thread(target=receiving, args=('name', s))
t.start()

while not shutdown:
    try:
        message = input()
        if message is not '':
            s.sendto(f"Server response --> {message}".encode('utf-8'), server)
        time.sleep(0.2)
    except:
        shutdown = True


t.join()
s.close()
