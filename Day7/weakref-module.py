# weak refernce allows to create an assignment to an object but not increase its reference count. 

class Dictator:
    pass

c=Dictator()
d=c
import sys
print(sys.getrefcount(c)) 

my_dict={}

import weakref
c=None
c=Dictator()
d=weakref.ref(c)
print(sys.getrefcount(c))

weak_c=my_dict
weak_d=weakref.ref(weak_c) # weakref has classes for dicts like weakDicts