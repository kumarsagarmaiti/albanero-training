# Abstraction is the concept in object-oriented programming that is used to hide the internal functionality of the classes from the users. Abstraction is implemented using the abstract classes. An abstract class in Python is typically created to declare a set of methods that must be created in any child class built on top of this abstract class. Similarly, an abstract method is one that doesn't have any implementation. abstract classes are used to create a blueprint of our classes as they don't contain the method implementation. This is a very useful capability, especially in situations where child classes should provide their own separate implementation. Also, in complex projects involving large teams and a huge codebase, It is fairly difficult to remember all the class names. An abstract method is a method that is declared, but contains no implementation. Abstract classes cannot be instantiated, and require subclasses to provide implementations for the abstract methods.

# We cannot create an abstract class in Python directly. However, Python does provide a module that allows us to define abstract classes. The module we can use to create an abstract class in Python is abc(abstract base class) module.

# Abstract methods force the child classes to give the implementation of these methods in them and thus help us achieve abstraction as each subclass can give its own implementation. A class containing one or more than one abstract method is called an abstract class.

# To define an abstract method we use the @abstractmethod decorator of the abc module. It tells Python that the declared method is abstract and should be overridden in the child classes.

# We can use the following syntax to create an abstract method in Python:

# from abc import ABC, abstractmethod
# class <Abstract_Class_Name>(ABC):
#     @abstractmethod
#     def <abstract_method_name>(self,other_parameters):
#         pass
# We just need to put this decorator over any function we want to make abstract, and the abc module takes care of the rest.

# The importance of using abstract classes in Python is that if our subclasses don’t follow that blueprint, Python will give an error. Thus we can make sure that our classes follow the structure and implement all the abstract methods defined in our abstract class. So, by using the abstract classes, we can ensure that our subclasses use the same structure and same method names for similar tasks. Also, by using the abstract classes, we can hide unnecessary details from the user and reduce the programming complexity to a great extent. A class that is derived from an abstract class cannot be instantiated unless all of its abstract methods are overridden.

# So, by using the abstract classes, we can ensure that our subclasses use the same structure and same method names for similar tasks. Also, by using the abstract classes, we can hide unnecessary details from the user and reduce the programming complexity to a great extent.

# Abstract Class Instantiation:
# Abstract classes are not complete, as they may have some methods that are not defined. So we cannot create an instance or object of an abstract class in Python. If we try to instantiate the abstract class, it raises an error.


# Invoke Methods from Abstract Classes
# Unlike some other programming languages, abstract Python methods don’t need to be completely abstract; they can have some basic-level implementation that can be used by all the concrete classes. A Concrete class is a class that has a definition for all its methods and has no abstract method.

# Concrete classes can use the super() to call the base abstract method and do some additional tasks into it. 

# Concrete classes can use the super() to call the base abstract method and do some additional tasks into it. 


from abc import ABC,abstractmethod

class Animal(ABC):
    
    # def __init__(self):
        # pass
    
    @property
    @abstractmethod
    def eats(self):
        pass
    
    @eats.setter
    @abstractmethod
    def eats_something_else(self,value):
        pass
        
    @abstractmethod
    def eats_what(self):
        print("coming from the abstract class")
    
class Dog(Animal):
    def __init__(self,eats):
        self.__eats=eats
        
    @property
    def eats(self):
        return self.__eats
    
    @eats.setter
    def eats_something_else(self,value):
        self.__eats=value
        
    def eats_what(self, eat):
        super().eats_what()
        print("coming from subclass")

jimmy=Dog("bone")
print(type(jimmy))
jimmy.eats_something_else="biscuits"
print(jimmy.eats_what("meat"))
print(jimmy.eats)
# print(jimmy.__eats)
print(jimmy.eats)

