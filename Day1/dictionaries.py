tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
# {'jack': 4098, 'sape': 4139, 'guido': 4127}
tel['jack']
# 4098
del tel['sape']
tel['irv'] = 4127
tel
# {'jack': 4098, 'guido': 4127, 'irv': 4127}
list(tel)
# ['jack', 'guido', 'irv']
sorted(tel)
# ['guido', 'irv', 'jack']
'guido' in tel
# True
'jack' not in tel
# False

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# {'sape': 4139, 'guido': 4127, 'jack': 4098}

# In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
{x: x**2 for x in (2, 4, 6)}
# {2: 4, 4: 16, 6: 36}

dict(sape=4139, guido=4127, jack=4098)
# {'sape': 4139, 'guido': 4127, 'jack': 4098}

my_map={
 1:2,
 10:2,
 5:3
}
print(my_map)