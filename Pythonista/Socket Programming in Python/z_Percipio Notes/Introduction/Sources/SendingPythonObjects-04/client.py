import socket
from product import Product
import pickle


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

	s.connect((socket.gethostname(), 4571))

	while True:
		
		msg = s.recv(1024)

		if not msg:
			print('No messages from the server. Closing the connection...')
			break

		product_object = pickle.loads(msg)

		print ('Product ID:', product_object.pid)
		print ('Product name:', product_object.pname)
		print ('Product price:', product_object.pprice, '\n\n')
