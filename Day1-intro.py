# print("Hello \nworld")

# width = 10
# height = 2
# print(width*height)

# words can be concatenated with '*' and '+' symbols
# print(3*"un"+"inium")

# Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.

# slicing allows you to obtain substring:
# word = "Hello"
# print(word[0:4])

# Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error:
# If you need a different string, you should create a new one:
# new_word = 'J' + word[1:]

# list = [1, 4, 9, 16, 25]
# copied_list = list[:]
# copied_list[0] = 0
# print(list)
# print(copied_list)
# You can also add new items at the end of the list, by using the append() method
# copied_list.append(36)
# print(copied_list)

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters)
# replace some values
# letters[2:5] = ['C', 'D', 'E']
# print(letters)
# ['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
# letters[2:5] = []
# print(letters)
# ['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
# letters[:] = []
# print(letters)
# []

# Fibonacci series:
# the sum of two elements defines the next
# a, b = 0, 1
# while a < 10:
#     print(a)
#     a, b = b, a+b

# Factorial:
# a, b = 1, 2
# while a < 10:
#     print(a)
#     a, b = b, a*b

# nums = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
#         14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
# flag = True
# for i in range(len(nums)):
#     for j in range(2, nums[i]):
#         if nums[i] % j == 0:
#             flag = False
#             break
#     if flag:
#         print(nums[i], "is a prime number")
#     else:
#         print(nums[i], "is not a prime number")
#         flag = True

# In a function call, keyword arguments must follow positional arguments. All the keyword arguments passed must match one of the arguments accepted by the function (e.g. actor is not a valid argument for the parrot function), and their order is not important. This also includes non-optional arguments (e.g. parrot(voltage=1000) is valid too). No argument may receive a value more than once. Here’s an example that fails due to this restriction:

# When a final formal parameter of the form **name is present, it receives a dictionary (see Mapping Types — dict) containing all keyword arguments except for those corresponding to a formal parameter. This may be combined with a formal parameter of the form *name (described in the next subsection) which receives a tuple containing the positional arguments beyond the formal parameter list. (*name must occur before **name.) For example, if we define a function like this:

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# Any formal parameters which occur after the *args parameter are ‘keyword-only’ arguments, meaning that they can only be used as keywords rather than positional arguments.

# Small anonymous functions can be created with the lambda keyword. Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition. Like nested function definitions, lambda functions can reference variables from the containing scope:

# def make_incrementor(n):
#     return lambda x: x + n

# f = make_incrementor(42)

#  Another use is to pass a small function as an argument:
# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])

# Recursive memoization function for fibonacci operations
fib_cache = {}


def fib(n: int):
    if n in fib_cache:
        return fib_cache[n]
    if n < 2:
        return n

    fib_cache[n] = fib(n-2)+fib(n-1)
    return fib_cache[n]

print(fib(15))

a1=[1,2,3]
a2=[4,5,6]
a1.extend(a2)
print(a1[0:len(a1)]+a2)
# *args
# **keywords

def some(a:int,b:int):
    return a+b

print(some('a','b')) 