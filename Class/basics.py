# Object-oriented programming is concerned with isolating concepts of a problem domain into separate entities and then using those entities to solve problems. Concepts related to a problem can only be considered once they've been identified. In other words, we can form abstractions from problems that make those problems easier to approach.

#  A class defines the attributes of objects, i.e., the information related to them (instance variables), and their commands, i.e., their methods. The values of instance (i.e., object) variables define the internal state of an individual object, whereas methods define the functionality it offers.
# A Method is a piece of source code written inside a class that's been named and has the ability to be called. A method is always part of some class and is often used to modify the internal state of an object instantiated from a class.
# An object is always instantiated by calling a method that created an object, i.e., a constructor by using the new or __init__ keyword.

# A class is an abstract blueprint that creates more specific, concrete objects. Classes often represent broad categories, like Car or Dog that share attributes. These classes define what attributes an instance of this type will have, like color, but not the value of those attributes for a specific object. Classes can also contain functions called methods that are available only to objects of that type. These functions are defined within the class and perform some action helpful to that specific object type. Class templates are used as a blueprint to create individual objects. These represent specific examples of the abstract class, like myCar or goldenRetriever. Each object can have unique values to the properties defined in the class.
# Benefits of OOP for software engineering
# OOP models complex things as reproducible, simple structures
# Reusable, OOP objects can be used across programs
# Polymorphism allows for class-specific behavior
# Easier to debug, classes often contain all applicable information to them
# Securely protects sensitive information through encapsulation

# Grouping related information together to form a class structure makes the code shorter and easier to maintain.

# Classes
# In a nutshell, classes are essentially user-defined data types. Classes are where we create a blueprint for the structure of methods and attributes. Individual objects are instantiated from this blueprint.
# Classes contain fields for attributes and methods for behaviors.

# Objects
# Objects are, unsurprisingly, a huge part of OOP! Objects are instances of a class created with specific data.

# Attributes
# Attributes are the information that is stored. Attributes are defined in the Class template. When objects are instantiated, individual objects contain data stored in the Attributes field.
# The state of an object is defined by the data in the object’s attributes fields.

# Methods
# Methods represent behaviors. Methods perform actions; methods might return information about an object or update an object’s data. The method’s code is defined in the class definition.
# When individual objects are instantiated, these objects can call the methods defined in the class.
# Methods are how programmers promote reusability and keep functionality encapsulated inside an object. This reusability is a great benefit when debugging. If there’s an error, there’s only one place to find it and fix it instead of many.

# Four Principles of OOP
# The four pillars of object-oriented programming are:

# Inheritance: child classes inherit data and behaviors from the parent class
# Encapsulation: containing information in an object, exposing only selected information
# Abstraction: only exposing high-level public methods for accessing an object
# Polymorphism: many methods can do the same task

# Inheritance
# Inheritance allows classes to inherit features of other classes. Put another way, parent classes extend attributes and behaviors to child classes. Inheritance supports reusability.

# If basic attributes and behaviors are defined in a parent class, child classes can be created, extending the functionality of the parent class and adding additional attributes and behaviors.
# You can access the parent class from inside a method of a child class by using super():
# The benefits of inheritance are programs can create a generic parent class and then create more specific child classes as needed. This simplifies programming because instead of recreating the structure of the Dog class multiple times, child classes automatically gain access to functionalities within their parent class.

# Encapsulation
# Encapsulation means containing all important information inside an object, and only exposing selected information to the outside world. Attributes and behaviors are defined by code inside the class template.

# Then, when an object is instantiated from the class, the data and methods are encapsulated in that object. Encapsulation hides the internal software code implementation inside a class and hides the internal data of inside objects.

# Encapsulation requires defining some fields as private and some as public.

# Private/ Internal interface: methods and properties accessible from other methods of the same class.
# Public / External Interface: methods and properties accessible from outside the class.
# Encapsulation adds security. Attributes and methods can be set to private, so they can’t be accessed outside the class. To get information about data in an object, public methods & properties are used to access or update data.

# This adds a layer of security where the developer chooses what data can be seen on an object by exposing that data through public methods in the class definition.

# Within classes, most programming languages have public, protected, and private sections. The public section is the limited selection of methods accessible from the outside world or other classes within the program. Protected is only accessible to child classes.

# Private code can only be accessed from within that class.
# Encapsulating & updating data: Since methods can also update an object’s data, the developer controls what values can be changed through public methods.

# This allows us to hide important information that should not be changed from phishing and the more likely scenario of other developers mistakenly changing important data.

# Encapsulation adds security to code and makes it easier to collaborate with external developers. When you’re programming to share information with an external company, you wouldn’t want to expose the classes’ templates or private data because your company owns that intellectual property.

# Instead, developers create public methods that allow other developers to call methods on an object. Ideally, these public methods come with documentation for external developers.

# The benefits of encapsulation are summarized here:

# Adds security: Only public methods and attributes are accessible from the outside
# Protects against common mistakes: Only public fields & methods are accessible, so developers don’t accidentally change something dangerous
# Protects IP: Code is hidden in a class; only public methods are accessible by the outside developers
# Supportable: Most code undergoes updates and improvements
# Hides complexity: No one can see what’s behind the object’s curtain!

# Abstraction
# Abstraction is an extension of encapsulation that uses classes and objects, which contain data and code, to hide the internal details of a program from its users. This is done by creating a layer of abstraction between the user and the more complex source code, which helps protect sensitive information stored within the source code.

# Abstraction

# Reduces complexity and improves code readability
# Facilitates code reuse and organization
# Data hiding improves data security by hiding sensitive details from users
# Enhances productivity by abstracting away low-level details
# Abstraction can also be explained using cars. Think of how a driver operates a vehicle using only the car’s dashboard.

# A driver uses the car’s steering wheel, accelerator, and brake pedals to control the vehicle. The driver does not have to worry about how the engine works or what parts are used for each movement. This is an abstraction – only the important aspects necessary for a driver to use the car are visible.

# Similarly, data abstraction allows developers to work with complex information without worrying about its inner workings. In this way, it helps to improve code quality and readability.
# Abstraction also serves an important security role. By only displaying selected pieces of data and only allowing data to be accessed through classes and modified through methods, we protect the data from exposure. To continue with the car example, you wouldn’t want an open gas tank while driving a car.

# The benefits of abstraction are summarized below:

# Simple, high-level user interfaces
# Complex code is hidden
# Security
# Easier software maintenance
# Code updates rarely change the abstraction


# Polymorphism
# Polymorphism means designing objects to share behaviors. Using inheritance, objects can override shared parent behaviors with specific child behaviors. Polymorphism allows the same method to execute different behaviors in two ways: method overriding and method overloading.

# Polymorphism means having many forms. Polymorphism enables using a single interface with different Python data types, different classes, or even a different number of inputs.

# Polymorphism is of two types:

# Run-time polymorphism
# Compile-time polymorphism
# Run-time Polymorphism
# Run-time polymorphism is the process in which the call to an overridden method is resolved at run-time. In Python, we implement run-time polymorphism through method overriding.

# Method overriding allows us to change the implementation of a method in the child class that is defined in the parent class.

# To override a method the following conditions must be met:

# There should be inheritance. The child class should be derived from the parent class.
# The method that we are redefining must have the same number of parameters as the method in the parent class.
# Example:

class Animal:
    def sound(self):
        print("Animal sound")


class Cat(Animal):
    def sound(self):
        print("Cat says meow")


animal = Animal()
cat = Cat()
animal.sound()
cat.sound()
# Output:

# Animal sound
# Cat says meow
# Compile-time polymorphism
# Compile-time polymorphism is the process in which the call to the method is resolved at the time of compilation. We implement compile-time polymorphism through method overloading.

# By using method overloading, you can implement the same functionality of the class with different parameters. Python does not support compile-time polymorphism but there is a workaround like an example below.

# Example:


class Example:
    def multiply(self, a, b, c=1):
        print(a*b*c)


example = Example()
example.multiply(5, 10)
example.multiply(2, 5, 6)
# Output:

# 50
# 60

# Method Overriding
# Runtime polymorphism uses method overriding. In method overriding, a child class can implement differently than its parent class.
# Method Overloading
# Compile Time polymorphism uses method overloading. Methods or functions may have the same name but a different number of parameters passed into the method call. Different results may occur depending on the number of parameters passed in.

# The benefits of Polymorphism are:

# Objects of different types can be passed through the same interface
# Method overriding
# Method overloading
