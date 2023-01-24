# Static Methods
# It is also possible to create a method that only applies to the class itself, not instances of the class. These can be distinguished with @classmethod and @staticmethod:

# Class Methods
# Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called.
# Because the class method only has access to this cls argument, it can’t modify object instance state. That would require access to self. However, class methods can still modify class state that applies across all instances of the class.

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
