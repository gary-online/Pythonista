import socket
import time

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    s.settimeout(0.2)

    s.bind((socket.gethostname(), 4571))

    i = 1

    while True:

        message = bytes('Message #' + str(i), 'utf-8')

        s.sendto(message, ('localhost', 37020))

        print('Message sent!')
        time.sleep(5)

        i += 1