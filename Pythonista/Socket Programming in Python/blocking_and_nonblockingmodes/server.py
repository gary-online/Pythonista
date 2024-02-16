from datetime import datetime
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((socket.gethostname(), 4571))
    s.listen(5)

    print('Server is up. Listening for connections...\n')

    client, address = s.accept()
    print('Connected to', address, 'established\n')
    print('Client object:', client, '\n')

    start_time = datetime.now()

    data = client.recv(1024)
    total_received_size = len(data)

    i = 1

    while data:
        print(data.decode('utf-8'))
        data = client.recv(1024)

        total_received_size += len(data)
        i += 1

    print ('All data received in %i batches' % i)

end_time = datetime.now()
print('Duration: ', end_time - start_time)

print('Size of data received: %i bytes' % total_received_size)