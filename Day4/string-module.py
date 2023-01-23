# The string module in python contains classes, utility functions and some constants for string manipulation.

from string import Template
import string

# string module constants
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.whitespace)
print(string.punctuation) 

s = "welcome ,to albanero"
print(s.capitalize())  # Capitilises the first letter only

print(string.capwords(s, ",")) # Capitilises the first letter of every word using str.split and str.join. The optional separator is used to split using the identifier.

# string module have two classes: Template and Formatter

# Formatter:
# The Formatter class in the string module allows you to create and customize your own string formatting behaviors using the same implementation as the built-in format() method.

# Template:
# This class is used to create a string template for simpler string substitutions.
# The Python string Template is created by passing the template string to its constructor. It supports $-based substitutions. This class has 2 key methods:

# substitute(mapping, **kwds): This method performs substitutions using a dictionary with a process similar to key-based mapping objects. keyword arguments can also be used for the same purpose. In case the key-based mapping and the keyword arguments have the same key, it throws a TypeError. If keys are missing it returns a KeyError.
k=Template("$hello $world")
# print(k.substitute(hello="hello",world="world"))
# safe_substitute(mapping, **kwds): The behavior of this method is similar to that of the substitute method but it doesn’t throw a KeyError if a key is missing, rather it returns a placeholder in the result string.

# The most important difference between Template and the rest of the string substitution tools available in Python is that the type of the argument is not taken into account. We can pass in any type of object that can be converted into a valid Python string. The Template class will automatically convert these objects into strings and then insert them into the final string.

# Using a Different Delimiter
# The class attribute delimiter holds the character used as the placeholder's starting character. As we've seen so far, its default value is $.

# Since the Python Template class is designed for inheritance, we can subclass Template and change the default value of delimiter by overriding it. Take a look at the following example where we override the delimiter to use # instead of $:


class MyTemplate(Template):
    delimiter = '#'


template = MyTemplate('Hi #name, welcome to #site')
print(template.substitute(name='Jane Doe', site='StackAbuse.com'))

# Output:
# 'Hi Jane Doe, welcome to StackAbuse.com'

# Escape operations also work
tag = MyTemplate('This is a Twitter hashtag: ###hashtag')
print(tag.substitute(hashtag='Python'))


t = Template('My name is $name and I work at $company')
s = t.safe_substitute(name="Kumar Sagar Maiti", company="albanero")
print(s)

# Changing What Qualifies as an Identifier:
# The idpattern class attribute holds a regular expression that is used to validate the second half of a placeholder in a template string. In other words, idpattern validates that the identifiers we use in our placeholders are valid Python identifiers. The default value of idpattern is r'(?-i:[_a-zA-Z][_a-zA-Z0-9]*)'.

# We can subclass Template and use our own regular expression pattern for idpattern. Suppose that we need to restrict the identifiers to names that neither contain underscores (_) nor digits ([0-9]). To do this, we can override idpattern and remove these characters from the pattern as follow:


# class MyTemplate(Template):
#     idpattern = r'(?-i:[a-zA-Z][a-zA-Z]*)'


# Underscores are not allowed
# template = MyTemplate('$name_underscore not allowed')
# print(template.substitute(name_underscore='Jane Doe'))
# If we run this code we will get this error:

# Traceback (most recent call last):
#     ...
# KeyError: 'name'
# We can confirm that digits are not allowed as well:

template = MyTemplate('$python3 digits not allowed')
print(template.substitute(python3='Python version 3.x'))
# The error will be:

# Traceback (most recent call last):
#     ...
# KeyError: 'python'

# If you decide to use a whole new regular expression for pattern, then you need to provide a regular expression with four named groups:

# escaped matches the escape sequence for the delimiter, like in $$
# named matches the delimiter and a valid Python identifier, like in $identifier
# braced matches the delimiter and a valid Python identifier using braces, like in ${identifier}
# invalid matches other ill-formed delimiters, like in $0site
# The pattern property holds a compiled regular expression object. However, it's possible to inspect the original regular expression string by accessing the pattern attribute of the pattern property. Check out the following code:

template = Template('$name')
print(template.pattern.pattern)
# \$(?:
#     (?P<escaped>\$) |   # Escape sequence of two delimiters
#     (?P<named>(?-i:[_a-zA-Z][_a-zA-Z0-9]*))      |   # delimiter and a Python identifier
#     {(?P<braced>(?-i:[_a-zA-Z][_a-zA-Z0-9]*))}   |   # delimiter and a braced identifier
#     (?P<invalid>)              # Other ill-formed delimiter exprs
#   )
# This code outputs the default string used to compile the pattern class attribute. In this case, we can clearly see the four named groups that conform to the default regular expression. As stated before, if we need to deeply customize the behavior of Template, then we should provide these same four named groups along with specific regular expressions for each group.

# The Hexadecimal, or Hex, numbering system is commonly used in computer and digital systems to reduce large strings of binary numbers into a sets of four digits for us to easily understand. Hexadecimal is used extensively in assembly programming languages and in machine code. It is often used to refer to memory addresses.
# The biggest advantage of the hexadecimal system is the compactness of its numbers, since fewer digits are required to represent a number than in binary or decimal notation. This is thanks to its base of sixteen. And it's relatively easy to convert binary numbers into hexadecimal numbers and vice versa.
