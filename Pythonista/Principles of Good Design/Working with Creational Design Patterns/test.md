Question: Which is true when you use the Builder design pattern?
Can parse complex structures to build the object
Separates object construction from representation

Question: While using the __new__() function to initialize a Singleton, if you want your object to be initialized only once and not each time __new__() is invoked what would you do?
Initialize the object the first time it is created in the __new__() special method

Question: The class which is the object pool i.e. holds the pool of instances available should be implemented using which design pattern?
The Singleton pattern

Question: Which of the following statements is true?
The abstract factory creates families of related objects
The factory pattern creates multiple objects by evaluating input parameters
The factory pattern is a creational design pattern

Question: Why might the Builder pattern be less useful when working with Python?
The use of default values for arguments make objects easy to create

Question: Which is true of the abstract factory design pattern?
Instantiates a family of related objects
Is closely related to the factory method pattern

Question: Which of the following is a reason to use the Object Pool design pattern?
Recycle instances rather than re-create instances
Allow only a limited number of instances to be in existence

Question: If you want the factory method to be abstracted from how each class is instantiated, which of the following is a valid technique to achieve this?
Have each class register a creation function with factory method

Question: While creating a Python object from a class i.e. instantiating an object, which is the right order in which special methods are invoked?
__new__() is invoked first and then __init__()

Question: Which is a correct explanation of the global object pattern in Python?
Set up a single instance of a class by keeping the class private to a module, initializing it once and then exposing it via a global variable

Question: Object pooling can be thought of as a more general purpose implementation of which pattern?
The Singleton pattern

Question: Which statement is NOT true about the factory method?
Cannot be used to instantiate derived classes of the same base class

Question: Of the options given below which option follows best practices in code design?
Code for different implementations should be refactored into separate methods

Question: Under what conditions might you choose to implement the Singleton design pattern?
The object is a global object with no clear owner
You want only one object of a class to be in existence
You want to lazily instantiate an object only when needed
