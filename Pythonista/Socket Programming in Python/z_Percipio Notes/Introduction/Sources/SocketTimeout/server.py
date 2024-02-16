import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

	s.bind((socket.gethostname(),4571))

	s.settimeout(10)
	
	s.listen(5)

	print('Server is up. Listening for connections...\n')

	client, address = s.accept()
	print('Connection to', address, 'established\n')
	print('Client object:', client, '\n')
	
	client.send(bytes('Hello! Welcome to socket programming.',"utf-8"))

