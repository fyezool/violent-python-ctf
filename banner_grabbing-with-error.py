import socket

s = socket.socket()

try:
    s.connect(("nowhere.samclass.info", 22))
    print(s.recv(1024).decode())
    s.close()
except socket.error as err:
    print(err)
