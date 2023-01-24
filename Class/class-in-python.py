# class Employee:
#     'Common base class for all employees'
#     empCount = 0

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1

#     def displayCount(self):
#         print("Total Employee %d" % Employee.empCount)

#     def displayEmployee(self):
#         print("Name : ", self.name,  ", Salary: ", self.salary)
# The variable empCount is a class variable whose value is shared among all instances of a this class. This can be accessed as Employee.empCount from inside the class or outside the class.

# The first method __init__() is a special method, which is called class constructor or initialization method that Python calls when you create a new instance of this class. __init__(). Every time a new Dog object is created, .__init__() sets the initial state of the object by assigning the values of the object’s properties. That is, .__init__() initializes each new instance of the class. You can give .__init__() any number of parameters, but the first parameter will always be a variable called self. The self-parameter refers to the current instance of the class and accesses the class variables. We can use anything instead of self, but it must be the first parameter of any function which belongs to the class. When a new class instance is created, the instance is automatically passed to the self parameter in .__init__() so that new attributes can be defined on the object.

# You declare other class methods like normal functions with the exception that the first argument to each method is self. Python adds the self argument to the list for you; you do not need to include it when you call the methods.

# To create instances of a class, you call the class using class name and pass in whatever arguments its __init__ method accepts.


# "This would create first object of Employee class"
# emp1 = Employee("Zara", 2000)
# "This would create second object of Employee class"
# emp2 = Employee("Manni", 5000)

# Every Python class keeps following built-in attributes and they can be accessed using dot operator like any other attribute −

# __dict__ − Dictionary containing the class's namespace.

# __doc__ − Class documentation string or none, if undefined.

# __name__ − Class name.

# __module__ − Module name in which the class is defined. This attribute is "__main__" in interactive mode.

# __bases__ − A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.

# Class Inheritance
# Instead of starting from scratch, you can create a class by deriving it from a preexisting class by listing the parent class in parentheses after the new class name.

# The child class inherits the attributes of its parent class, and you can use those attributes as if they were defined in the child class. A child class can also override data members and methods from the parent.

# Syntax
# Derived classes are declared much like their parent class; however, a list of base classes to inherit from is given after the class name −

# class SubClassName (ParentClass1[, ParentClass2, ...]):
#    'Optional class documentation string'
#    class_suite
# You can use issubclass() or isinstance() functions to check a relationships of two classes and instances.

# The issubclass(sub, sup) boolean function returns true if the given subclass sub is indeed a subclass of the superclass sup.

# The isinstance(obj, Class) boolean function returns true if obj is an instance of class Class or is an instance of a subclass of Class

# There are different forms of inheritance depending on the structure of inheritance taking place between a derived class and a base class in Python. Let’s discuss each one of them individually:

# Single inheritance: The type of inheritance when a class inherits only one base class is known as single inheritance, as we saw in the above example.
# Multiple inheritance: When a class inherits multiple base classes, it’s known as multiple inheritance. Unlike languages like Java, Python fully supports multiple inheritance. All the base classes are mentioned inside brackets as a comma-separated list.
# Multilevel inheritance: When a class inherits a base class and then another class inherits this previously derived class, forming a ‘parent, child, and grandchild’ class structure, then it’s known as multilevel inheritance. Example:
class BaseClass():
    def __init__(self):
        print("Base class")
class childClass(BaseClass):
    def __init__(self):
        print("Child class")
class grandchildClass(childClass):
    def __init__(self):
        BaseClass.__init__(self)
        childClass.__init__(self)
        print("Grand child class")
ob1 = grandchildClass()

# Hierarchical inheritance: When there is only one base class inherited by multiple derived classes, it is known as hierarchical inheritance.
# Hybrid inheritance: Hybrid inheritance is when there is a combination of the above-mentioned inheritance types, that is, a blend of more than one type of inheritance.

# Overriding Methods
# You can always override your parent class methods. One reason for overriding parent's methods is because you may want special or different functionality in your subclass.

# Sr.No.	Method, Description & Sample Call
# __init__ ( self [,args...] ):
# Constructor (with any optional arguments)
# Sample Call : obj = className(args)

# __del__( self ):
# Destructor, deletes an object
# Sample Call : del obj

# __repr__( self ):
# Evaluable string representation
# Sample Call : repr(obj)

# __str__( self ):
# Printable string representation
# Sample Call : str(obj)

# __cmp__ ( self, x ):
# Object comparison
# Sample Call : cmp(obj, x)

# Overloading Operators
# Suppose you have created a Vector class to represent two-dimensional vectors, what happens when you use the plus operator to add them? Most likely Python will yell at you.

# You could, however, define the __add__ method in your class to perform vector addition and then the plus operator would behave as per expectation −

# class Vector:
#    def __init__(self, a, b):
#       self.a = a
#       self.b = b

#    def __str__(self):
#       return 'Vector (%d, %d)' % (self.a, self.b)

#    def __add__(self,other):
#       return Vector(self.a + other.a, self.b + other.b)

# v1 = Vector(2,10)
# v2 = Vector(5,-2)
# print v1 + v2 #This will print(7,8)

# Data Hiding
# An object's attributes may or may not be visible outside the class definition. You need to name attributes with a double underscore prefix, and those attributes then are not be directly visible to outsiders.

# Private Attributes of a Class in Python
# While implementing inheritance, there are certain cases where we don’t want all the attributes of a class to be inherited by the derived class. In those cases, we can make those attributes private members of the base class. We can simply do this by adding two underscores (__) before the variable name.

# Example:

# class Base1:
#     def __init__(self):
#         self.x = 10
# # creating a private variable named y
#     def __init__(self):
#         self.__y = 5
# class Derived1(Base1):
#     def __init__(self):
#         self.z = 20
#         Base1.__init__(self)
# ob1 = Derived1()
# print(ob1.y)


# class JustCounter:
#     __secretCount = 0

#     def count(self):
#         self.__secretCount += 1
#         print(self.__secretCount)


# counter = JustCounter()
# counter.count()
# counter.count()
# AttributeError: JustCounter instance has no attribute '__secretCount'
# print(counter.__secretCount)

# Python protects those members by internally changing the name to include the class name. You can access such attributes as object._className__attrName. If you would replace your last line as following, then it works for you −

# print counter._JustCounter__secretCount

# Class Properties
# In Python, a property in the class can be defined using the property() function.

# The property() method in Python provides an interface to instance attributes. It encapsulates instance attributes and provides a property, same as Java and C#.

# The property() method takes the get, set and delete methods as arguments and returns an object of the property class.

# The following example demonstrates how to create a property in Python using the property() function.

# Example: property() Copy
class Student:
    def __init__(self):
        self.__name=''
    def setname(self, name):
        print('setname() called')
        self.__name=name
    def getname(self):
        print('getname() called')
        return self.__name
    name=property(getname, setname)
# In the above example, property(getname, setname) returns the property object and assigns it to name. Thus, the name property hides the private instance attribute __name. The name property is accessed directly, but internally it will invoke the getname() or setname() method, as shown below.

# Example: property() Copy
# >>> std = Student()
# >>> std.name="Steve"
# setname() called
# >>> std.name
# getname() called
# 'Steve'

# Types of Classes in Python
# There are various types of classes in Python in which some are as follows:

# Python Abstract class
# Python Concrete class
# Python Partial Class

# Python Abstract Class
# An abstract class is a class that contains one or more abstract methods. The term “abstract method” refers to a method that has a declaration but no implementation. When working with a large codebase, it might be difficult to remember all classes. That is when a Python Abstract class can be used. Python, unlike most high-level languages, does not have an abstract class by default.

# A class can be defined as an abstract class using abc.ABC, and a method can be defined as an abstract method using abc.abstractmethod. The abbreviation for abstract base class is ABC. The ABC module, which provides the foundation for building Abstract Base classes, must be imported. The ABC module operates by decorating base class methods as abstract. It installs concrete classes as the abstract base’s implementations.

# Example:

# From abc import ABC, abstractmethod
# Class AbstractClassName(ABC):
# @abstract method
# def abstract_method_name(self):
# Pass
# Python Concrete class
# Concreate classes have only concrete methods but abstract classes can have both concrete methods and abstract methods. The concrete class implements abstract methods, but the abstract base class can also do so by initiating the methods through super ().

# Python Partial Class
# The partial class is one of the python classes. We can use it to develop a new function that only applies a subset of the statements and keywords you pass to it. You can use partial to freeze a chunk of your function’s statements and/or keywords, resulting in the creation of a new object. We can use the Functools module to implement this class.

# Mutable and Immutable Objects in Python
# A mutable object is a changeable object that can be modified after it is created. Lists, dict, set and byte array are all mutable objects.

# An immutable object is an object whose state can never be modified after it is created.  Int, float, complex, Python string, tuple, frozen set, and bytes are immutable.

# Python handles mutable and immutable objects in different ways. Mutable objects are of great use in scenarios where there is a need to change the object size. Immutable objects are used when you want an object you created to always stay the same as it was when created.