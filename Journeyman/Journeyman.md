In a test script, you have the following code:
python
from unittest import TestCase
import src.shape_area as area

class TestShapeArea(TestCase):

    def test_triangle(self):
        self.assertEqual(area.ShapeArea.triangle(5, 10), 25)

    def test_rectangle(self):
        self.assertEqual(area.ShapeAre.rectangle(6, 7), 42)

    def test_square(self):
        self.assertEqual(area.ShapeArea.square(6), 36)

What is the result when you run this code?
The test case will pass

Review the following excerpt from a URL:
/skillsoft/form1.php?name1=value1&name2=value2
Which type of REST API method is being used? 
GET

You have created a script named four_test.py that contains four different tests, which are as follows:


test_1()
test_2()
test_3()
test_4()

You want to run the fourth test from this script. Which command should you use?
pytest four_test.py::test_4

You have created a script that contains four different tests. When you execute the script with the pytest command, all tests pass successfully; however, you want to determine the order in which the tests are executed.
Which command should you use?
pytest -v

With the given code, what is the output that is displayed on the Webpage when you load it using Flask?
<!DOCTYPE html>
<html lang="">
  <head>
    <title>Welcome</title>
  </head>
  <body>
    Hello World!
  </body>
</html>
Hello World!

Review the following code:


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_feedback(url)
        app.logger.debug('stored feedback: ' + url)

What is the purpose of using app.logger.debug method?
Records the submitted feedback in the logs

When you implement multithreading, which benefits are achieved? [Choose all that apply.]
Threads share memory space
Threads share CPU cores
Threads are lightweight

Which statements are true if a thread is granted exclusive access to a resource? [Choose all that apply.]
The output of the application is consistent
There are no race conditions

In the following script, how many tests are run?


import unittest
import rectangle_perimeter

class TestArea(unittest.TestCase):

    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter.get_perimeter)
 
    @unittest.skip('Temporarily skips error test')
    def test_error(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter.get_perimeter(10, 5) 

if __name__ == 'main__':
    unittest.main()
Only the first test

What is the purpose of importing the OS module in the following code?


import os
from multiprocessing import process, current_ process
Helps to provide the process details

What is the output of this code?


import queue
from collections import deque

q = queue.Queue()
q.queue
deque([])
for i in range(7):
    q.put(i)
q.queue
print(q.empty())
False

Which HTTP status code is displayed if you attempt to access a resource that does not exist?
404

In the following code, what type of object does feedback represent?


from flask import Flask, render_template

app = Flask(__name__)
feedback = []

def store_feedback(url):
    pass
List

When using the REST API, which verb should be used to update or replace an existing resource?
PUT

Review the following code:


import queue

q = queue.PriorityQueue()
q.put(5)
q.put(4)
q.put(1)
q.put(3)
q.put(2)
while not q.empty():
    print(q.get())

What is the output?
1
2
3
4
5

You have built a small Web application in Flask. You want to connect it with a database. To create the database, you include the following code in the app.py file:


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

Where does the site.db file get created?
In the same directory where app.py is stored

You want to dynamically build a URL in Flask. Which function should you use?
url_for()

You have written a test script with a single test case that you execute from the terminal window using the following command:


python testcase.py

After you execute the script, which of the following output indicates the successful run of the test?
A single dot

You run a test script with three test cases. You execute the script form the terminal window using the following command:


python testcase.py

After you execute the script, you get the following result:


F..

What does this output denote?
The first of the three tests have failed

In the pytest environment, when are you likely to run fixtures?
Before and after the actual test functions

Which methods of a condition object can be called only after the calling thread has acquired a lock? [Choose all that apply.]
notify()
wait()
notifyAll()

What is the output of the following code?


import asyncio

async def greetings(message):
    for i in range(6):
        print(message)
        await asyncio.sleep(1)

asyncio.run(greetings("Hello"))
asyncio.run(greetings("World"))
Hello
Hello
Hello
Hello
Hello
Hello
World
World
World
World
World
World

Which Python package is used for making HTTP requests?
Requests

You have implemented the semaphore mechanism on a video server. If the limit for a particular resource is reached, what happens when a task requests to access it?
The task will wait for its turn to access the resource

Review the following Python test script:


def test_type():
    assert type(1 + 2) is int

def test_add_int():
    assert 5 + 2 == 7

def test_string():
    assert 'u' in 'sun'

def test_add_string():
    assert ('sunny' + 'day') == 'sunnyday'

You run pytest from the directory that this script is stored. Which test is executed first?
test_type()

A script named simple_test.py contains the following code:


import pytest

@pytest.mark.number
def test_type():
    assert type(1 + 2) is int

@pytest.mark.number
def test_add_int():
    assert 5 + 2 == 7

@pytest.mark.string
def test_string():
    assert 'u' in 'sun'

@pytest.mark.string
def test_add_string():
    assert ('sunny' + 'day') == 'sunnyday'

You want to execute the tests that are associated with the number marker. Which pytest command option should you use?
-m

Your system has a CPU with four cores. If you run the following code, how many unique processes are created?


from multiprocessing import Pool

def cal_square(n):
    return n * n

num_list = [1, 2, 3, 4, 5]
result = []
for num in num_list:
    result.append(cal_square(num))

p = Pool()
result = p.map(cal_square, num_list)
p.close()
4

To make a GET request, you have imported three packages using the following commands:


import requests
from pprint import pprint
import json

You want to verify the version of the requests package. Which of the command should you use?
print(requests.__version__)

A user requests a Webpage from a Webserver on the Internet. After receiving the request, what is the next step that the Webserver performs?
Checks the header of the request

You have a script named shape_area.py that contains the following code:


import doctest

doctest.testfile(""shape_area_readme.txt"")

What is the output when you execute this script?
It executes the contents of the referenced text file

Which version of Python introduced the asyncio module?
3.4

You are creating a REST API web service. When you run Flask, which file will it run by default?
app.py

Which of the following are used to enclose multi-line docstrings?
"""
"""

Which of the following are features of a dynamic Websites? [Choose all that apply.]
Ability to query databases for the requester content
Ability to generate HTML based on specific requests
Ability to customize the user experience by maintaining sessions
Ability to re-use elements across multiple pages on a site

Which HTTP status code is returned when a requested page been temporarily moved and traffic is redirected to the provided URL?
302

In the Flask environment, you want to customize the existing Webpage using certain colors and fonts. Which file should you edit for this purpose?
main.css

On a Linux system, you have a root folder with two levels of nested folders. Each folder includes several Python-based test scripts. You want to execute all of them at once using pytest.
From the root directory

When implementing multithreading, which conditions can cause a deadlock? [Choose all that apply.]
Mutual exclusion
No pre-exemption
Hold and wait
Circular wait

You have created a database with the following code in the app.py file:

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

You have also created a table within the database and want to verify that the table was created. Which command would you execute from a Linux/macOS terminal?
less site.db

Using Python code, you want to determine the number of CPU cores in your system. After importing the OS class, which code segment should you use?
os.cpu_count()

When executing tasks in a linear fashion, which statements are true? [Choose all that apply.]
When each task is completed, the next one is started immediately
Some tasks may require long waits, which results in inactivity

You want to use Flask as the Webserver application framework for a Web application. What are the benefits of using Flask? [Choose all that apply.]
Well-documented
Extensible
Scalable
Microframework

Consider the following code:


import time
import threading
from pprint import pprint

def sleeping_func():
    time.sleep(2)
    print("\nHello from sleeping_fun!")

x = threading.Thread()
x.start()
x = threading.Thread(target = sleeping_func)
x.start()

pprint(threading.active_count())
print()
pprint(threading.enumerate())
print()
pprint(threading.current_thread()

When is the sleeping_func() likely to execute?
All functions are executed before the sleeping_func() function

Which statement is true about the following code?


import threading
from pprint import pprint

def new_func():
    pprint(threading.active_count())
    print()
    pprint(threading.enumerate())
    print()
    pprint(threading.current_thread())
It will list all the running threads
It will count the running threads
It will list the current thread

You have the pytest environment configured on your Mac laptop. You have installed PyCharm. After installation, which task is mandatory for you to complete?
Set the project interpreter

You are making a POST request using the following code:


POST /test/form1.php HTTP/1.1
Host: skillsoft.com
name1=value1&name2=value2

Where will the POST request be stored when it is being sent to the server?
In the request body of the HTTP request

Which statements describe the properties of multithreading? [Choose all that apply.]
Concurrent threads are in a partially completed state
Multiple tasks are executed concurrently by the same process
Only one thread is being worked on at any given time

Which statement about threads in Python is true?
The Python interpreter can run code from one thread at a time

You have written a script named test_student.py that contains five different tests that perform different operations. The initial part of the script contains the following code that includes two functions other than the five tests:


import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.stu_1 = Student('Robin', 'Wills', '25000')
        self.stu_2 = Student('Mark', 'Smith', '28000')

    def tearDown(self):
        pass

In the given code, how many times does the teardown function run?
Five times

Review the following code:


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

From the Python Shell, you enter the following:


>>> from app import User
>>> user_regular = User(username='user', email='suser@loonycorn.com', password='loony')

What will happen when you create the user?
An id is generated by the database and the default.jpg file is used

In the Flask environment, you attempt to access a route that has not been defined. What is the result?
An error message is displayed

Review the following code:


import threading
import time

def greetings_1():
    for i in range(6):
        print("Hello")
        time.sleep(1) 

def greetings_2():
    for i in range(6):
        print("World")
        time.sleep(1)

start_time = time.time()
tl = threading.Thread(target = greetings_1)
t2 = threading.Thread(target = greetings_2)
tl.start()
t2.start()
tl.join()
t2.join()
end_time = time.time()
print("Total time:", end_time - start_time)

Which statement best describes the result of this code?
All threads run concurrently

Which statements are true for performing multiprocessing in Python? [Choose all that apply.]
It can be performed with a multi-core processor
It can be done on a system with multiprocessors

You have executed the following command in the Flask environment:


pip install flask-bcrypt

Which of the following does flask-bcrypt help you achieve?
To calculate the hash for the passwords

After running the flask-bcrypt utility, you get the following output:


b'$2b$12$Js4hdJZ8BpIz860C5JLZk.3CqzppmB9SNuyGPBbUBjsZr71SMbUAG'

Which of the following is generated?
Password hash

You want to run a series of comprehensive automated tests on API endpoints. Which of the following will serve this purpose?
pytest

You have the Flask environment running. In the app.py file, you have added the code to create a database and a table named site.db. From the Python Shell, you type the following:


>>> from app import db
>>> db.create_all()
>>> from app import User
>>> user_regular = User(username='user', email='user@loonycorn.com', password='loony')
>>> db.session.add(user_regular)

What is the status of the user account being created?
The user is created in the session but not written to the database

Consider the code below:


import requests
from pprint import pprint

r_head = requests.head('http://google.com', allow_redirects=True)
print(r_head.status_code)

What does an output of 200 indicate?
A successful request

Which statements describe the features of the Flask framework? [Choose all that apply.]
It enables HTML templating with Jinja
It includes a built-in development server
It is compliant with WSGI specification
It is a Web framework written in Python

In your Flask application, you have not specified a category when flashing a message to the user. Which default category is used?
message



















