import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

	client_name = input('Enter your name: ')

	sock.connect((socket.gethostname(), 4571))
	sock.send(client_name.encode())

	server_name_raw = sock.recv(1024)
	server_name = server_name_raw.decode()
	print('You have connected to the server %s' %server_name)

	while True:

		message_recv = sock.recv(1024)
		message_recv = message_recv.decode()
		print(server_name, ' - ', message_recv)

		send_message = input(client_name +' - ')
		sock.send(send_message.encode())

		if send_message.lower() == "bye":
			break