import socket
from product import Product

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	
	s.connect((socket.gethostname(), 4571))

	while True:
		msg = s.recv(1024)

		if not msg:
			print('No messages from the server. Closing the connection...')
			break
			
		print('Message from server:', msg.decode('utf-8'))
		print('Type of received message:', type(msg))
