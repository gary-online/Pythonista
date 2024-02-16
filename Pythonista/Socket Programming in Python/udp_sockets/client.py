import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    s.bind(("", 37020))

    while True:

        data, addr = s.recvfrom(1024)
        print('Received message:', data)