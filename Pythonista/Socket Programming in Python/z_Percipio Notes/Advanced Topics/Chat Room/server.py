import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    server_name = input('Enter your name: ')

    sock.bind((socket.gethostname(),4571))

    sock.listen(5)
    print(server_name, 'is up. Listening for connections...\n')
    
    client, address = sock.accept()
    print('Connection to', address, 'established\n')
    print('Client object:', client, '\n')

    client_name_raw = client.recv(1024)
    client_name = client_name_raw.decode()
    print('Client %s has initiated a connection.' %client_name)

    client.send(server_name.encode())

    while True:

        send_message = input(server_name +' - ')
        client.send(send_message.encode())

        if send_message.lower() == "bye":
            break

        message_recv = client.recv(1024)
        message_recv = message_recv.decode()
        print(client_name , '-', message_recv)
        