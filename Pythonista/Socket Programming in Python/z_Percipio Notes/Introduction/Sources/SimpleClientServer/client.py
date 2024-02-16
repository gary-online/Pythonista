import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 4571))

msg = s.recv(1024)
print('Message from server:', msg.decode('utf-8'))

s.close()