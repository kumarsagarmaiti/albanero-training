#  An enumeration is a set of members that have associated unique constant values. Enumeration is often called enum.
# Create a new enumeration by defining a class that inherits from the Enum type of the enum module.
# The members have the same types as the enumeration to which they belong.
# Use the enumeration[member_name] to access a member by its name and enumeration(member_value) to access a member by its value.
# Enumerations are iterable.
# Enumeration members are hashable.
# Enumerable are immutable.
# Cannot inherits from an enumeration unless it has no members.

from enum import Enum


class Animal(Enum):
    DOG = 1
    TIGER = 2
    CAT = 3
    LEOPARD = 4


# animal=Animal()
# Cannot instantiate an Enum sub-class


print(Animal.DOG.name)  # DOG
print(Animal.DOG.value)  # True
print(type(Animal.DOG))  # <enum 'Animal'>
print(type(Animal))  # <class 'enum.EnumMeta'>
print(Animal.DOG)
print(Animal(2))  # Animal.TIGER

# Enum subclasses are needed because they have a set of members containing unique constant values. Enumerations are immutable: once an Enum subclass is defined it cannot be modified from inside or any new members can be inserted or old members deleted. We can access the members of the enumeration.
# Enum classes are iterable. For example:
for animal in Animal:
    print(animal)

# even though the above method is correct the below method should be followed in case there is an alias having the same value.
# for name, member in Colour.__members__.items():
    # print(name, member)
# Enumerations do not support inheritance unless it has no members.
# Enumerations can be hashed. Why hashing needed?
# Why enum needed
# Enums can only be compared to enums and not any other string or value even if they have the same value
# We can know the corresponding constant using the value.

# Magic Number: A unique value with unexplained meaning or multiple occurrences which could (preferably) be replaced with a named constant. A constant numerical or text value used to identify a file format or protocol; for files

# In essence, if you have magic numbers in your code, you should definitely consider to either assign them to a variable or group them together to an enumeration. This way your code's readability increases a lot. It is especially true if you want to write tests for your code.

# response_code.py

# from http_code_enum import HTTPCode
# from http.client import HTTPResponse


# def evaluate_response(response: HTTPResponse) -> str:
#     if response.code() == HTTPCode.NOT_FOUND:
#         return "Not Found"
#     elif response.code() == HTTPCode.BAD_GATEWAY:
#         return "???"
#     elif response.code() == HTTPCode.BAD_REQUEST:
#         return "???"
#     else:
#         return "Unknown Status Code"

# Why not tuple: We dont know or may not remember the index and value inside the tuple. So we will have to iterate to get the index of a particular value. Same with dictionaries. In enum we can get the constant by just passing the value. 
