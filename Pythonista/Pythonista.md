# Question: Which principle states that once you have written a class, you should never modify it after that?
The Open/Closed Principle

# Question: In a Web application that you are building, you do not want the clients to use an object or a resource directly. Instead, you want access to the objects or resources to be directed or gated through an object. What should you do?
Implement a proxy object

# Question: Identify the design pattern that is being used in this code:

Code Editor:
class ConnectionPool:

    __instance = None

    def __new__(cls, num_connections):
        if cls.__instance is None:
            print('No instance exists, creating a new one')

        cls.__instance = super(ConnectionPool, cls).__new__(cls)

        cls.__instance.__num_connections = num_connections
        cls.__instance.__connections = []

        for i in range(num_connections):
            cls.__instance.__connections.appendConnection())

        else:
            print('A previously created instance exists, returning that same one')

        return cls.__instance
    def acquire(self):
        for i in range(self.__num_connections):
            connection = self.__connections[i]

            if not connection.is_used():
                connection.acquire()
                return connection

### Instruction: Choose the option that best answers the question.  
Singleton pattern

# Question: Which statements describe the characteristics of design patterns? [Choose all that apply.]
Improve the quality of design
Improve the speed of development
Solve a specific known problem

# Question: Identify the pattern being used in the following code:

Code Editor(Python):
class LegacyRectangle:

    def __init__(self, length, breadth):

        self.__length = length
        self.__breadth = breadth

    def area_calculation(self):
        return self.__length * self.__breadth

    def draw(self):
        print("This draws a legacy rectangle to screen")

one_rectangle = LegacyRectangle(5, 6)
print(one_rectangle.area_calculation())

Adapter pattern

# Question: You are working on a MAC system. You want to get access to the BSD socket interface on the system. Which Python package should you install?
sudo pip install sockets

# Question: After installing PyCharm, you need to create a JSON file. You right-click on the project that you had created and then select New. Which option should you select afterward to create the JSON file?
File

# Question: You want to work with images using the openpyxl Python library. Which openpyxl package contains the image module?
drawing

# Question: What is the result of the following code?

Code Editor(Python):
socket.gethostbyname(socket.gethostname())

### Instruction: Choose the option that best answers the question. 
The IP address of the system

# Question: Review the following code:

Code Editor(Python):
class LegacyRectangle:

    def __init__(self, length, breadth):

        self.__length = length
        self.__breadth = breadth

    def area_calculation(self):
        return self.__length * self.__breadth

    def draw(self):
        print("This draws a legacy rectangle to screen")

one_rectangle = LegacyRectangle(5, 6)
print(one_rectangle.area_calculation())

### What is the output?

30

# Question: What is the result of the following code?

Code Editor(Python):
import openpyxl

work_book = openpyxl.Workbook()
work_book.active
<Worksheet "Sheet">
sheet = work_book['Sheet']
sheet['A1'] = 'Hello'
sheet['B1'] = 'Excel'
sheet['C1'] = 'Users!'

### Instruction: Choose the option that best answers the question.
It will write the values in the respective columns

# Question: You are using the following code to parse JSON data in the PyCharm IDE:

Code Editor (Python):
for json_element in data:
    if (json_element['price'] == None):
        print("error occurred at \n", json_element)
        continue

if int(json_element['price'] < 50):
    csv_string = return_csv(json_element)
    writer.writerow(json_element)

## Which statements describe the correct output? [Choose all that apply.]
Rows where price has no value are printed to the console
The code executed with exit code 0

# What is the significance of s.listen(5) in the following code?

Code Editor:
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((socket.gethostname(),4571))
    s.listen(5)
    print('Server is up. Listening for connections...\n')

It will set up the connection to listen to five different connection

# Question: Which Python module provides support for networking and inter process communication?
socket

# Question: You are building an interactive Webpage that has several events linked with the different components on your Webpage. However, do not want to slow down the performance of the Webpage.
## What should you do?
Configure centralized event handling using the flyweight pattern

# Question: What does AF_INET signify in the given code?
Code Editor:
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

The address on which the socket will communicate

# Question: Which statements describe the correct use cases for the Object Pool pattern? [Choose all that apply.]
When the number of objects in use at a time is low
When the rate of object instantiation is high
When the cost of initializing objects is high

# Review the following code:

Code Editor(Python):
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((socket.gethostname(),4571))
    s.listen(5)

    print('Server is up. Listening for connections...\n')

    client, address = s.accept()
    print('Connection to', address, 'established\n')
    print('Client object:', client, '\n')

    client.send(bytes('Hello! Welcome to socket programming.',"utf-8"))


### What is the duration for which the server application will listen for the clients' incoming connections?
Will listen indefinitely

# Question: In an Excel sheet, you have the following values:
A1=2
A2=2
A3=2
A4=2
A5=2

### You execute the following command:
Code Editor(Python):
sheet[ 'C3' ] = 'PRODUCT:'
sheet[ 'D3' ] = '=PRODUCT(A1:A5)'

### What is the correct output?
32

# Question: Review the following code statements and identify the correct statement.
Code Editor(Python):
from openpyxl.styles import NamedStyle
custom_style = NamedStyle(name="header")
custom_style.font = Font(bold=True)
custom_sytle.border = Border(bottom=Side(border_style="thin"))
custom_style.alignment = Alignment(horizontal="center", vertical="center")

### Instruction: Choose the option that best answers the question. 
Only the header in the current worksheet row is impacted

# Question: Which namespace is being used in the given commands?
Code Editor(Python):
import openpyxl
from openpyxl.chart import LineChart, Reference

openpyxl.chart

# Question: In an Excel workbook, you want to freeze all rows above the current cursor location, and all left columns to the cursor location should be frozen. Which option should you choose?
Freeze Panes

# Question: You have a set of engineering data. You need to compare certain numeric values. Which chart type is most suitable for such a comparison?
Scatter Chart

# Question: When using the Python socket module, which task is performed each time you invoke the send function?
The data is sent to the socket directly

# Question: You have imported the openpyxl library in Jupyter Notebook. You execute the following code:
Code Editor(Python):
cell = sheet_obj['B1']
type(cell)

### What is the output?
openpyxl.cell.cell.Cell

# Question: Which principle states that the derived types must be completely substitutable for their base types?
Liskov’s Substitution Principle

# Question: In an Excel worksheet, you need to refer to a set of cells. However, you do not want to refer to them with the cell range. What another method can you use?
Create a named range

# Question: Which design pattern is being used in this code?
Code Editor(Python):
from abc import abstractmethod
 
class Operation:
    def __init__(self, successor=None):
        self.__successor = successor
 
    @abstractmethod
    def calculate(self, operation):
        pass

class Exponent(Operation):
    def calculate(self, operation):
        chars = operation.split()
 
        if chars[1] == '**':
            print('Exponent!')
            return int(chars[0]) ** int(chars[2])

        elif self._successor is not None:
            print('Exponent unable to handle operation, passing on to successor')
            return self._successor.calculate(operation)

        else:
            print("Operation not supported")
            return None

### Instruction: Choose the option that best answers the question. 
Chain-of-Responsibility pattern

# Question: Which design pattern is being used in this code?

Code Editor:
from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class Bold(Command):

    def execute(self):
        print('Bold')

    def undo(self):
        print('Undo Bold')

### Instruction: Choose the option that best answers the question. 
Command pattern

# Question: In Excel, you want to add the values in five consecutive cells, A1 to A5, using the SUM formula. What is the correct method of writing the SUM formula?
=SUM(A1:A5)

# Question: Which design pattern follows the Hollywood principle of "Don’t call us, we’ll call you"?
Observer pattern

# Question: Which Python package provides image processing capabilities that will allow you to break an image into chunks before transmitting it from one Python app to another?
Pillow

# Question: Which of the following are characteristics of the abstract factory pattern? [Choose all that apply.]
Creates an instance of any one of many families of classes
Aims to encapsulate a group of individual factories that have a common goal

# Question: Which Design pattern is being used in the given code?
Code Editor(Python):
class Product():
 
    @staticmethod
    def create(item_name, *args(:
 
        if item_name == 'MacBookAir':
            return MacBookAir(*args)
        elif item_name == 'AppleIPad':
            return AppleIPad(*args)
        elif item_name == 'AppleIWatch':
            return AppleIWatch(*args)

### Instruction: Choose the option that best answers the question.
Simple Factory

# Question: You have the pytest environment configured on your Mac laptop. You have installed PyCharm. After installation, which of the following tasks is mandatory for you to configure?
Set the project interpreter

# Question: When using the Python socket module, which mode is used when the sending application waits for the buffer to have space before it writes data into it?
Blocking mode

# Question: Which design pattern encapsulates a request as an object?
Command pattern

# Question: You are implementing a design pattern that handles requests using a single pipeline that passes the right object handler's requests. Which design pattern are you implementing?
Chain-of-Responsibility pattern

# Question: Which feature in the PyCharm IDE can be used to change the name of a variable or a function?
Refactoring

# Question: Using the openpyxl Python library, you want to retrieve the content of a particular cell. Which command should you use?
cell.value

# Which principle enforces the high-level objects to push information to the low-level objects via events?
The Hollywood Principle

# Question: You are using the openpyxl Python library. In the given command, data from how many columns are being referenced?

Code Editor(Python):
values = Reference(sheet, min_col = 2, min_row = 2, max_col = 2, max_row = sheet.max_row)

### Instruction: Choose the option that best answers the question. 
1

# Question: Which design pattern allows you to set up a class's behavior that is not fully defined at runtime?
Decorator pattern

# Question: You are executing code in PyCharm and want to examine the intermediate state of the application. Which feature can help you achieve this goal?
Breakpoints

# Question: You have run the following code in Jupyter Notebook:

Code Editor(Python):
import openpyxl

## You want to edit an existing Excel workbook. Which function should you use to open the workbook?

### Instruction: Choose the option that best answers the question. 
openpyxl.load_workbook

# Question: Which types of bar charts are available in Excel? [Choose all that apply.]
Histogram
Box and Whisker

# Question: Which Design pattern is being used in this code?

Code Editor(Python):
class Payment:
 
    def pay(self, amount):
        pass
 
class BankAccount(Payment):
 
    def __init__(self, balance):
        self.__balance = balance
        self.__card = None
 
    def set_card(self, card):
        self.__card = card
 
    def __has_funds(self, amount):
        print("Checking whether funds are available")
 
        if amount <= self.__balance:
            return True
 
        return False
 
    def pay(self, amount):
        if self.__has_funds(amount):
            print("Bank: paying the merchant", amount)
            self.__balance -= amount
            return Ture
        else:
            print("Bank: payment declined, you don’t have enough funds")
            return False

### Instruction: Choose the option that best answers the question. 
Proxy pattern

# Question: Which design pattern defines a family of algorithms that achieve the same objective?
Strategy pattern

# Question: You have an Excel workbook that contains a date column. You want to change the formatting of the dates that are present in the date column. Which shortcut keys should you use to invoke the Format Cells dialog box?
Ctrl + 1

# Question: Which statements are true for the given code? [Choose all that apply.]

Code Editor(Python):
wb = openpyxl.load_workbook('datasets/tech_stocks.xlsx')
sheet = wb.active
multi_line_chart = LineChart()
multi_line_chart.title = "Facebook vs. Netflix"
multi_line_chart.x_axis.title = "Time(Sep-2018 to Sep-2019)"
multi_line_chart.y_axis.title = "Price(US$)"
values = Reference(sheet, min_col=2, min_row=1, max_col=3, max_row=sheet.max_row)
multi_line_chart.add_data(values, titles_from_data=True)

### Instruction: Choose the option that best answers the question.
It will create a bar chart
It will include only two columns for the chart
It will include data from all given rows

# Question: Which principle states that the client should not be forced to implement unnecessary methods that they will not use?
Interface Segregation Principle

# Question: You have an existing object that matches certain specifications. You want to create other objects of the same type. Which design pattern should you use?
Prototype pattern

# Question: You are using the openpyxl Python library to format data in an Excel file.

Code Editor(Python):
for row in sheet['K2:M101']:
    for cell in row:
        cell.number_format = '#,##0'

## In the given code, what does 0 represent in ‘#,##0’?

### Instruction: Choose the option that best answers the question. 
It represents numbers that you want Excel to display

# Question: When you apply the Singleton pattern in your code, how many instance(s) of a class or function can you create?
1

# Question: What is the result of the following code?
A new blank workbook is opened

# Question: Which principle focuses on building components that should not know or talk to the other components?
Principle of Least Knowledge

# Question: Which principle states that a class should do one thing and do it well?
Single Responsibility Principle

# Question: You want to parse Excel formulas using the openpyxl Python library. Which package should you use?
formula

# Question: Which design pattern is not concerned with expressing relationships between objects?
Adapter pattern

# Question: Which design pattern instantiates a single global object and provides a global point of access to this object?
Singleton pattern


















