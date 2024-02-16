;Review the following code:

class Student:
    name = ""
    email = ""
    school = None

object_1 = Student()
object_1.name = Michel
object_1.email = 'Michel@xyz.com'
object_1.school = 10

Which code segment will cause an error?

    object_1.name = Michel
    
What is the purpose of the following code?

class LinkedList:
   def __init__(self):
       self.head = None
       
    To initialize the head node variable to None
Which types are classified as linear data structures? [Choose all that apply.]

    Queue
    Stack
    Array
You have created a custom module and want to make it distributable. To do this, which file must you create?

    setup.py
Which implementation of sorting uses an insertion sort and divides the entire list into sublists, which are sorted?
    
    Shell sort
Review the following code

print(int.__add__(1, 2))

What is the output of this code?

    3
Consider the following code:

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass

x = Student("Josh", "Fairbanks")
x.printname()

What is the purpose of using the pass statement on line 09?

    It does not require you to add any properties for the Student class
Which of the following should you use to create a custom data type in Python?

    Class
When using an analogy of a house, which of the following represents a blueprint?

    Class
Which statements are true of a binary search in Python? [Choose all that apply.]

    It is a method that starts in the middle of a sorted list to start the search for the element
    Is a method to search for an element in a list to check every element until you find the right one
What is the result of the following code?

class Competition:
    def __init__(self, name, prize):
        self.__name = name
        self.__prize = prize

rowing = Competition('Rowing', 10000)
print(rowing)

    The memory location of the object is printed on the screen
Which Queue methods are considered to be O(1) operations? [Choose all that apply.]

    empty()
    qsize()
    full()
Which type of sort chooses one element, finds the smallest element, and then makes the smallest element the first element?

    Selection sort
Identify the outcome of the following code:

class Competition:
    __raise_amount = 1.10

    def __init__(self, name, prize):
        self.__name = name
        self.__prize = prize
    def get_name(self):
        return self. name
    def get_prize(self):
        return self.__prize
    def raiseprize(self):
        self.__prize = self.__prize * self__raise_amount
    
race = Competition('Race', 100)
print(type(race))

    <class'__main__.Competition'>
On the Python shell, you enter the following command:


4 // 2

What is the result?

    2

Which of element in a linked list points to the null value, assuming that the list is not empty?

    Tail

Which of the following is equivalent to O(N^2)? [Choose all that apply.]

    O(N^2 + N)
    O(N^2 + 1000)
Review the following code:

def print_list(num_list):
    print(num_list)

def my_sort(original_list):
    
    length = len(original_list)
    
    for i in range(0, length - 1):
        for j in range(i + 1, 0, -1):       
            if original_list[j] < original_list[j - 1]:
                original_list[j], original_list[j - 1] = original_list[j - 1], original_list[j]

        print('Sorted till index: ', i)
        print_list(original_list)

a = [10, 5, 7, 2, 8, 3, 9, 6, 1, 4]
my_sort(a)

Which type of sort is being implemented?

    Insertion sort
You have a Binary Search Tree with a root node and several other nodes with their children. You need to insert a new node into the Binary Search Tree.

Which action should you perform first?

    Compare the node to be inserted with the root of the tree
Review the following code:

def lookup(head, data):
    if head == None:
        return print("Value not found!")
    if head.get_value() == data:
        return head
    if data <= head.get_value():
        return lookup(head.get_left_child(), data)
        return lookup(head.get_right_child(), data)

What does the code represent?

    Binary Search Tree
How many iterations are performed in the following code?

def addition(num1, num2):
    num_iterations = 0
    total = num1 + num2
    num_iterations += 1
    print("The sum of %d and %d is %d \nTotal number of iterations = %d"%(num1, num2, total, num_iterations))

addition(10, 4)

    1
You want to avoid referring to the parent class explicity when calling its methods from a child class. Which function should you use?

    super()
Review the following code:

while True:
    try:
        input_var = int(input("Please enter a number: "))
        break
        print("Good choice")
    except ValueError:
        print("Oops! That was not a valid number. Try again… " )
print("Thanks")

What is the result if 'one' is inputted?

    Oops! That was not a valid number. Try again...
    Please enter a number:
Which implementation of sorting is considered to be highly efficient when using the divide and conquer approach?

    Insertion sort
Which of the following can be attributes of a class? [Choose all that apply.]

    Variables
    Functions
In the Python command shell on a Windows system, you enter the following commands:

import sys
sys.path

What is the expected result?

    Path of the Python source directory
In the Binary Search Tree structure, what is the maximum number of children that a node can have?

    2
You have defined a method in a child class with the same name as a method in the parent class. What is the outcome?

    The parent method will be overridden

You are working on a Jupyter notebook that has been set up on a MacOS system. You want to execute a shell command. Which of the following should you prefix with the shell command?

    !
Which of the following statements are true for an abstract class in Python? [Choose all that apply.]

    Several abstract classes are included in Python
    In can be used for large functional unites
    Subclasses can implement its methods
You are defining a Binary Search Tree. In the following code, how many pointers are being defined?

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    2
You have a text file that has 100 characters. You want to find the current cursor position in a file that is not opened in append mode. Which of the following value is returned?

    0
Which statements are true about the following code?

class Student:
    def __init__(self, name):
        self.name = name
        self.mail = name + "." + "@xyz.com"
        
    One arguement is required when instantiating Student
    The self parameter is mandatory
    __init__ is a function defined in the Student class
Which questions are likely to be asked on sorting in an interview? [Choose all that apply.]

    Do equal elements maintain their original order after sorting?
    How does the sort scale when the input size increases?
    Is the sort stable?
    Does the sorting need extra space to hold information?
    Is the sort adaptive?
Where can an element be removed from a stack in Python?

    From the top of the list
Which type of sort focuses on the pivot rather than the length of an artificial index list?

    Quick sort
Which of the following can you include in a module? [Choose all that apply.]

    Functions
    Variables
    Classes
You have a Python 2 script that you want to convert to Python 3. After conversion, you should be able to run the script in the Python 3 environment. Which tool should you use to convert this script?

    2to3
Which of the following statements are true for classes in Python? [Choose all that apply.]

    It is a building block that can model two types of information about an entity
    It is a building block that can model only one type of relationship
    It is a building block that models real-world relationships
When performing the breadth-first traversal, which task are you likely to perform?

    You visit every node at one level before moving to the next level
What is the result of running the following code?

try:
    print(variable)
except NameError:
    print("Variable is not defined")
except:
    print("An unknown error has occurred")
    
    The first except block is executed
What is the outcome of the given code?

class MethodFloordiv:
    def __init__(self, number):
        self.number = number
    def __floordiv__(self, other):
        return self.number // other.number

num_1 = MethodFloordiv(10)
num_2 = MethodFloordiv(3)
result = num_1 // num_2
print(result)

    3
What is the result of the following code:

try:
    print(var)
except:
    print("Incorrect")
finally:
    print("Game Over")
    
    Both Incorrect and Game Over are printed to the console
Review the following code:

class MethodSub:
    def __init__(self, number):
        self.number = number
    def __sub__(self, other):
        return self.number + other.number

num_1 = MethodSub(10)
num_2 = MethodSub(8)
print(num_1 - num_2)

What is the output?

    18
Which statements are correct of an adjacency list? [Choose all that apply.]

    It points to a linked list
    Each vertex is a node
In the following code, which type of sort is being implemented?

def print_list(num_list):
    print(num_list)
    
def sort(original_list):
    
    length = len(original_list)
    
    for i in range(length):

        min_value_index = i

        for j in range(i + 1, length):

            if original_list[min_value_index] > original_list[j]:
                min_value_index = j
        
        original_list[i], original_list[min_value_index] = original_list[min_value_index], original_list[i]

        print('Sorted till index: ', i)
        print_list(original_list)

    print('Sorted list: ')
    print_list(original_list)

num_list = [10, 11, 5, 7, 2, 8, 3, 9, 6, 1, 4]
sort(num_list)

    Selection sort
Which statements are true for static methods? [Choose all that apply.]

    It is always present in a class
    It cannot access or modify a class state
Review the following code:

from queue import Queue
olympics = Queue(5)
olympics.put('United States(USA)')
olympics.put('Great Britain(GBR)')
print(olympics.empty())

What is the result?

    False
In the depth-first traversal, how many sub-trees are involved with a recursive step?

    2
You have a file named sample.txt that contains the following text:

Hello Everyone!
Welcome to Skillsoft
You are learning file operations
Have a good time
Goodbye

To read from this file, you execute the following commands:

file = open("sample.txt")
file.seek(0)
print(file.read(5))

What is the output?

    Hello
An algorithm whose complexity does not change with the input size is O(1). The algorithm is said to have constant _____________ complexity.

    time
Which are the correct methods to access the class variables? [Choose all that apply.]

    By prefixing the name of the class to the variable
    By prefixing the name of the object instance
Which metrics can be used to measure the performance of an algorithm? [Choose all that apply.]

    Memory usage
    Bandwidth consumption
    Number of operations
Which statements are true of the adjacency matrix? [Choose all that apply.]

    Each cell represents the relationship between the vertices
    It uses a matrix with rows and columns
Which type of sort compares each element first with its neighbors and swaps the elements so that the smaller one is earlier in the list?

    Bubble sort
You have installed Anaconda with Python 3; however, you want to be able to run old Python 2 code in Jupyter Notebook. What should you do?

    Create a Conda virtual environment for Python 2
In the following code, what type of variable is __raise_amount?

class Competition:
    __raise_amount = 1.10

    def __init__(self, name, prize):
        self.__name = name
        self.__prize = prize
    def get_name(self):
        return self. name
    def get_prize(self):
        return self.__prize
    def raiseprize(self):
        self.__prize = self.__prize * self__raise_amount
        
    Class
You have a file named sample.txt that contains the following text:

Hello Everyone!
Welcome to Skillsoft
You are learning file operations
Have a good time
Goodbye

To read from this file, you execute the following commands in Juypter Notebook:

file = open("sample.txt")
file.seek(0)
file.read(6)
print(file.readline())

What is the output?

    Everyone!
Which function provides access to the methods and properties of a parent class?

    super()
Which type of graph is being defined in the following code?

from graph import *
from queue import Queue
import numpy as np
 
def first(graph, start=0):
 
    queue = Queue()
    queue.put(start)
 
    visited = np.full((graph.num_vertices, ), False, dtype=bool)
 
    while not queue.empty():
        vertex = queue.get()
 
        if visited[vertex]:
            continue
 
        print("Visited: ", vertex)
        visited[vertex] = True
 
        for v in graph.get_adjacent_vertices(vertex):
            if not visited[v]:
                queue.put(v)
                
    Breadth-first traversal