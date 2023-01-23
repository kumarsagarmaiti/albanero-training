# Classes provides a means of bundling data and functions together. It creates a new type of object, allowing new instances of that type to be made. It has attributes and methods attached to it. Methods can be used to modify the state of the class.

# Namespaces:
# A namespace is mapping of names to objects. It is in a dictionary format. Examples of namespaces are: the set of built-in names (containing functions like abs(), and built-in exception names), the global names in a module, the local names when a function is called. Two different modules have two different namespaces. They both can have a function with the same name but the module name has to be different.
# A namespace can have different creation time and lifetime. The namespace containing the built-in (built-in names live inside the builtin module) names are created when python interpreter starts up, and is never deleted. The global namespace for a module is created when the module is in read-in. Global namespaces normally also lasts until the interpreter quits. The statements executed by the top level invocation of the interpreter are considered part of the __main__ module, so they have their own namespace.
# The local namespace of a function is created when the function is called and destroyed after execution. Recursive functions each have their own name spaces.

# W.R.T objects the attribute is any name that follows the dot. For example in z.real real is an attribute of the z object. Attributes can be readable and writable as well. Assigning value to an attribute is possible. Module attributes are writable. Writable attributes can be deleted with the 'del' keyword.

# Scope:
# A scope is a textual region in Python where a namespace is directly accessible. Although scopes are defined statically they can be used dynamically. That means the namespace is directly accessible starting from local scope and going till global scope.
# An enclosed function searches for a name in the order: Local-->Enclosed-->Global-->Built-in and if it still doesn't find it, it will throw a NameError.

# x = 10
# def outer():
#     y = 5

#     def inner():
#         print(y)
#         print(x)
#     inner()


# outer()
# print(y) ->Gives a NameError
import sys
import os
spam1 = 10


def scope_test():
    def do_local():
        spam = 12

        print(spam)

        def do_nonlocal():
            nonlocal spam  # to change the nonlocal variable we use the nonlocal keyword followed by the name we want to change. If keyword not given it throws an error
            spam = spam+2
        do_nonlocal()
        print("After non-local assignment:", spam)

    def do_global():
        global spam1  # UnboundLocalError: local variable 'spam' referenced before assignment. This error happens because we try to modify a global name inside a scope.To do that we need to use the global keyword followed by the name.
        spam1 = spam1+1

    # spam = "test spam"
    do_local()
    # print("After local assignment:", spam)
    # do_nonlocal()
    # print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam1)


scope_test()
print("In global scope:", spam1)

# Class:
# The statements inside class are usually function definitions, but other statements are also allowed.
# A class definition like a function definition need to be executed before they have any effect. For every class definition a namespace is created.
# Class objects supports two kind of operations: attribute references and instantiation. Class attributes are called similarly as that of object attributes with a dot(.) notation.


# class MyClass:
#     """A simple example class"""
#     i = 12345

#     def f(self):
#         return 'hello world'

# MyClass.i and MyClass.f are valid attribute references, returning an integer and a function object, respectively. Class attributes can also be assigned to, so you can change the value of MyClass.i by assignment. __doc__ is also a valid attribute, returning the docstring belonging to the class: "A simple example class".


# Class instantiation uses a function notation. Class is instanstiated as such:
# This creates a new instance of the class and assigns this object to the variable x.
# x = MyClass()

# The instance created creates an empty object. To create an object with a predefined initial state we use the __init__ special method.


class MyClass:
    def __init__(self, value):
        self.data = [value]
        self.val = value
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

    def showVal(self):
        return self.val


x = MyClass(9)

print(x.showVal())


class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)                  # shared by all dogs
print(e.kind)                  # shared by all dogs
print(d.name)                  # unique to d
print(e.name)                  # unique to e
# The class variable should be immutable or it will be shared by all class instances. For example:


class Dog:

    # tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name
        self.tricks = []  # correct way is to use instance variable

    def add_trick(self, trick):
        self.tricks.append(trick)


# In methods the instance object is passed as the first argument of the method. So method can be stored in a variable and called later. In general, calling a method with a list of n arguments is equivalent to calling the corresponding function with an argument list that is created by inserting the method’s instance object before the first argument.
x = MyClass(10)
xf = x.f

print(xf())

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)                # unexpectedly shared by all dogs

# Data attributes overide the method attributes if both have the same name.
print(os.getcwd())
os.system("touch standard-library.py")

print(sys.argv)


class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self,sound):
        return f"{self.name} is an animal which speaks {sound}"


class Dog(Animal):
    def __init__(self,name):
        self.name=name
    def speak(self,sound="woofs"):
        # return f"{self.name} woofs"
        return super().speak(sound)

jimmy=Animal("Jimmy")
print(jimmy.speak("woof"))
print(jimmy.speak("hello"))
tommy=Dog("Tommy")
print(tommy.speak())