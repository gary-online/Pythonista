import socket
from product import Product
import pickle
import time

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

	s.bind((socket.gethostname(),4571))

	custom_objects = [Product('P024', 'Torch', 13),
					  Product('P025', 'WaterBottle',5 ),
					  Product('P026', 'KeyBoard', 20),
					  Product('P027', 'Mouse', 15),
					  Product('P028', 'USBCable', 2)]
	

	s.listen(5)

	print('Server is up. Listening for connections...\n')

	client, address = s.accept()
	print('Connection to', address, 'established\n')
	print('Client object:', client, '\n')


	for product in custom_objects:
			
		pickled_product = pickle.dumps(product)
		client.send(pickled_product)

		print('Sent product: ', product.pid)

		time.sleep(2)




