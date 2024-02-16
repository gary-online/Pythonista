## Install the sockets module
pip install sockets --upgrade

## Display the contents of the /etc/hosts file
less /etc/hosts

## Bring up the python shell to show the socket object
python

import socket

socket.gethostname()
# 'development'

socket.gethostbyname(socket.gethostname())
# '10.0.0.203'

socket.gethostbyaddr('10.0.0.203')

socket.gethostbyname('')
# '0.0.0.0'

exit()

####################################################################
####################################################################

## SimpleClientServer
# Create the server.py and client.py files
# From a new tab, run the server
python server.py

# The server is now listening for connections
# Run the client so that it can receive the message sent by the server
python client.py


####################################################################
####################################################################

## SocketWith
## Modify the client.py and server.py files to use the with context manager
# Re-run the two scripts to show that they work just as they did before
python server.py

python client.py

####################################################################
####################################################################

## SocketTimeout
## In the server.py file, add the line for settimeout
# Restart the server
python server.py

# Wait enough time for the timeout to expire. A timeout error is raised and printed to the console
# Restart the server
python server.py

# Bring up the client before the timeout expiration. It works as it did before
python client.py

####################################################################
####################################################################

## SocketTimeoutException
## Modify the server.py file to use the try-except block
# Restart the server
python server.py

# Wait enough time for the timeout to expire. A timeout error is raised and handled
# Restart the server
python server.py

# Bring up the client before the timeout expiration. It works as it did before
python client.py


####################################################################
####################################################################

## SendingPythonObjects-01
## Modify the server.py file so that it tries to send a python dictionary as well as a custom object
## The server now does not have a timeout either

# Restart the server
python server.py

# Bring up the client. The data is received as bytes
# For this data to be useful, it needs to be in the form of the object which was sent
python client.py


####################################################################
####################################################################

## SendingPythonObjects-02
## Modify the server.py file so that the data sent is not cast as bytes

# Restart the server
python server.py

# Bring up the client. There is an error at the server:
# TypeError: a bytes-like object is required 
python client.py


####################################################################
####################################################################

## SendingPythonObjects-03
## Modify the server.py file to use pickle to serialize the data
## The client.py file also uses pickle to deserialize the Python objects

# Restart the server
python server.py

# Bring up the client. 
# The types of the data sent and received is visible
# The types before and after serialization/deserialization is printed
python client.py


####################################################################
####################################################################

## SendingPythonObjects-04
## The client.py file now references the objects

# Restart the server
python server.py

# Bring up the client. 
# The client is able to use the objects transmitted 
python client.py


####################################################################
####################################################################

## SendingPythonObjects-05
## The server.py file now references the list of objects
## It will iterate over the list and send one object at a time
## Modify the server to import the time module, and to send the list of Products
import time

# Restart the server
python server.py

# Bring up the client. 
# The client is able to use the list of objects transmitted 
python client.py




