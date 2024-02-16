import socket
from PIL import Image

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((socket.gethostname(), 4571))
    s.listen(5)
    print('Server is up. Listening on port 4571...\n')

    client, address = s.accept()
    print('Connected to', address, 'established\n')
    print('Client object:', client, '\n')

    with open('server_files/gary_codes.png', 'rb') as image_file:

        image_batch = image_file.read(40960)

        while image_batch:
            client.send(image_batch)
            image_batch = image_file.read(40960)
            print('One batch sent to the client...')

print('Image sent successfully')