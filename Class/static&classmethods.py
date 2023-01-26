
# Instance method performs a set of actions on the data/value provided by the instance variables. If we use instance variables inside a method, such methods are called instance methods.


# Static Methods
# Static method is a general utility method that performs a task in isolation. This method doesn’t have access to the instance and class variable. It can neither modify the object instance state or the class state.

# Class Methods
# Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called. Therefore, it belongs to a class level, and all class instances share a class method.
# Because the class method only has access to this cls argument, it can’t modify object instance state. That would require access to self. However, class methods can still modify class state that applies across all instances of the class.
# Class method Used to access or modify the class state. It can modify the class state by changing the value of a class variable that would apply across all the class objects.
# Class methods are used as a factory method. Factory methods are those methods that return a class object for different use cases. For example, you need to do some pre-processing on the provided data before creating an object.
# The class method uses cls as an argument to point to the class instead of the constructor. Therefore, if we decide to rename the class at some point we won’t have to remember updating the constructor name in all of the classmethod factory functions.
# We can use the factory functions to create new class objects that are configured the way we want them. They all use the same __init__ constructor internally and simply provide a shortcut for remembering all of the various ingredients. Another way to look at this use of class methods is that they allow you to define alternative constructors for your classes. Python only allows one __init__ method per class. Using class methods it’s possible to add as many alternative constructors as necessary. This can make the interface for your classes self-documenting (to a certain degree) and simplify their usage.

# As this method do not apply to the instances of the class, they can be accessed without instantiating the class.

import math
from datetime import date as dt


class Home:
    name = "Code Ninja"
    rooms = 4
    stories = 2

    @staticmethod
    def is_on_market(home):
        if (home.name == "Home"):
            return True
        else:
            return False

    @classmethod
    def paint_wall(cls, color):
        return f"Painting wall with the color {color}."


# The Static methods are used to do some utility tasks, and class methods are used for factory methods. The factory methods can return class objects for different use cases.
# The static methods cannot change the state of the class but the class method takes the class as parameter to know about the state of that class.


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def isAdult(age):
        if age > 18:
            return True
        else:
            return False

    @classmethod
    def emp_from_year(cls, name, year):
        return cls(name, dt.today().year - year)

    def __str__(self):
        return 'Employee Name: {} and Age: {}'.format(self.name, self.age)


e1 = Employee('Dhiman', 25)
print(e1)
e2 = Employee.emp_from_year('Subhas', 1987)
print(e2)
print(Employee.isAdult(25))
print(Employee.isAdult(16))

home = Home()
# home.name="Home"
print(Home.is_on_market(home))
# Output: False

# TODO: Inheritance based on static and class method.


class Pizza:

    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

    @classmethod
    def circle_diameter(cls, radius):
        return cls(radius, radius*2)


p = Pizza(4, ['mozzarella', 'tomatoes'])
print(p)
print(p.area())
print(p.circle_area(7))
print(p.circle_diameter(3))

# As we’ve learned, static methods can’t access class or instance state because they don’t take a cls or self argument. That’s a big limitation — but it’s also a great signal to show that a particular method is independent from everything else around it.
# Flagging a method as a static method is not just a hint that a method won’t modify class or instance state — this restriction is also enforced by the Python runtime.

# Techniques like that allow you to communicate clearly about parts of your class architecture so that new development work is naturally guided to happen within these set boundaries. Of course, it would be easy enough to defy these restrictions. But in practice they often help avoid accidental modifications going against the original design.

# Put differently, using static methods and class methods are ways to communicate developer intent while enforcing that intent enough to avoid most slip of the mind mistakes and bugs that would break the design.

# Applied sparingly and when it makes sense, writing some of your methods that way can provide maintenance benefits and make it less likely that other developers use your classes incorrectly.

# Static methods also have benefits when it comes to writing test code.

# Because the circle_area() method is completely independent from the rest of the class it’s much easier to test.

# We don’t have to worry about setting up a complete class instance before we can test the method in a unit test. We can just fire away like we would testing a regular function. Again, this makes future maintenance easier.


class Dog:
    gender = "male"

    def __init__(self, age, name="Doggy"):
        self.age = age
        self.name = name

    @staticmethod
    def is_name_doggy(name):
        if name == "doggy":
            return True
        return False

    @staticmethod
    def print_gender():
        return Dog.gender

    @classmethod
    def change_gender(cls, gender):
        cls.gender = gender

    @classmethod
    def make_dog(cls, str):
        name = str.split(" ")[-1]
        age = None
        return cls(age, name)


str_1 = "My dog's name is Tommy"
new_dog_1 = Dog.make_dog(str_1)
# Dog.change_gender("female")
# new_dog_1.gender="female"
print(new_dog_1.gender)
print(new_dog_1.is_name_doggy("tommy"))
print(Dog.is_name_doggy("tommy"))
print(new_dog_1.name)


class Poodle(Dog):
    gender = "Female"


str_2 = "My dog name Jimmy"
new_dog_2 = Poodle.make_dog(str_2)
# Poodle.change_gender("male")
print(new_dog_2.gender)
print(new_dog_2.name)
print(Poodle.is_name_doggy("doggy"))
