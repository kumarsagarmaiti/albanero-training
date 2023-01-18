# A tuple consists of a number of values separated by commas, for instance:
t = 12345, 54321, 'hello!'
# t[0] -> 12345
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
# ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# Tuples are immutable:
t[0] = 88888
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
# ([1, 2, 3], [3, 2, 1])
