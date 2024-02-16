

## SendingPythonFiles
## The server.py file now references the a file in the server_files folder
## Confirm that there is a client_files folder which is empty 
## File source https://www.kaggle.com/tentotheminus9/religious-and-philosophical-texts/version/1#pg2680.txt


# Restart the server
python server.py

# Bring up the client. 
# The client is able to use the File transmitted 
python client.py

#The received_file is saved in the client_files folder


####################################################################
####################################################################

## SendingPythonImages
## There is a new image file in server_files. Source of the image:
## https://www.pexels.com/photo/adorable-animal-breed-canine-356378/
## The client.py file now references the Image object

#Importing the Image module from PIL library in the code
from PIL import Image

# Restart the server
python server.py

# Bring up the client. 
# The client is able to use the objects transmitted 
python client.py

#The received_img is saved in the same folder


####################################################################
####################################################################

## ChatRoom
## This is a continuous transmission of data in between server and client

# Restart the server
python server.py

# Bring up the client. 
# The client.py file now receives and sends the data to the server
python client.py


####################################################################
####################################################################



## BlockingMode
## Set the client in Blocking mode.
## The time taken to excute the code is greater when blocking is set

#To show the time taken for execution we import the below module
from datetime import datetime

# Restart the server
python server.py

# Bring up the client. 
# The client.py sends the data to the server
python client.py


####################################################################
####################################################################

## NonBlockingMode
## Unset the blocking mode. In Non-Blocking mode the time taken to execute the same code is quite less.

#The difference of the time taken in both modes can be compared. 
from datetime import datetime



# Restart the server
python server.py

# Bring up the client. 
# The client.py sends the data to the server
python client.py


## Do one more run of the server and client apps
## The data received by the server will likely be different from the previous run
python server.py

python client.py



####################################################################
####################################################################

## RSSFeeds
## The RSS feeds of the given URL will be displayed 
## You will need to install feedparser for this demo
pip install feedparser --upgrade

## View RSS feed details in a Python shell

python 

import feedparser

feed = feedparser.parse('https://news.un.org/feed/subscribe/en/news/topic/economic-development/feed/rss.xml')

type(feed)

dir(feed)

feed['href']
feed.href

feed.entries
len(feed.entries)

feed.entries[0]
feed.entries[0].title
feed.entries[0].link
feed.entries[0].summary

exit()

## Move to the source file where you refresh the RSS feed periodically
#For parsing of the feed we use feedparser module
import feedparser

# Bring up the client. 
# Give the URL and the client displays the neewfeed for the same
python client.py


####################################################################
####################################################################

## UDPSockets
## Prepare the server.py and client.py source files

## Start the server.py file and wait for 2-3 messages to be sent
python server.py
 
## Start the client.py. It will receive all the new messages
python client.py 

## Stop the server by hitting Ctrl-C. The client is still up
## Re-start the server after a few seconds. The client begins receiving messages again
python server.py 


