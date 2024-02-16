import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((socket.gethostname(),4571))
    s.listen(5)
    print('Server is up. Listening for connections...\n')
    
    client, address = s.accept()
    print('Connection to', address, 'established\n')
    print('Client object:', client, '\n')

    custom_file = open('server_files/meditations.txt', 'rb')

    custom_data = custom_file.read(40960)

    while (custom_data):
            client.send(custom_data)
            custom_data = custom_file.read(40960)
    
    print('Custom File succesfully Sent')