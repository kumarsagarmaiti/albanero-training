# Python’s memory management algorithm uses a reference counting mechanism for garbage collection, which tracks all reachable objects. All Python objects include a reference count field, which counts how many objects are referencing it. If an object is referenced by another object, then its counter is set to a non-zero number and the object can’t be garbage collected. If the counter reaches zero, the garbage collector will free that object.
# To create weak references in python, we need to use the weakref module. The weakref is not sufficient to keep the object alive. A basic use of the weak reference is to implement cache or mappings for a large object.

# Not all objects can be weakly referenced. Some built-in types like tuple or int, do not support weak reference. There are some classes and methods related to weak reference.

# Class weakref.ref(object[, callback])
# It will return a weak reference to the object. When the referent is still alive, the actual object can be retrieved by calling the reference object, but when the actual object is not present, it will return None.

# Method weakref.proxy(object[, callback])
# This method is used to return a proxy for the object, which are using weak reference. The returned object may be either ProxyType or CallableProxyType.

# Method weakref.getweakrefcount(object)
# This method is used to return the number of weak references and proxies of the objects.

# Method weakref.getweakrefs(object)

# This method is used to return a list of weak references and proxies objects.


# Python’s memory management algorithm uses a reference counting mechanism for garbage collection, which tracks all reachable objects. All Python objects include a reference count field, which counts how many objects are referencing it. If an object is referenced by another object, then its counter is set to a non-zero number and the object can’t be garbage collected. If the counter reaches zero, the garbage collector will free that object. 

# Sometimes a large object is stored in the cache so there is no need to keep it alive. Let’s you have a large number of image objects and they are being used as keys to map to images due to which these objects will be kept alive. 

# Fortunately, weakref module provides something called as WeakKeyDictionary and WeakValueDictionary doesn’t keep the objects alive as they appear in the mapping objects.

# The following classes and methods are provided by weakref module:

# class weakref.ref(object[, callback])  – This returns a weak reference to the object.
# weakref.proxy(object[, callback]) – This returns a proxy to object which uses a weak reference.
# weakref.getweakrefcount(object) – Return the number of weak references and proxies which refer to object.
# weakref.getweakrefs(object) – Return a list of all weak reference and proxy objects which refer to object.

import weakref


class my_list(list):
    pass


new_list = my_list('String')  # Use my_list class to define a list
print(new_list)
weak_ref = weakref.ref(new_list)
new_weak_list = weak_ref()
new_proxy = weakref.proxy(new_list)
print(new_weak_list)
print('The object using proxy: ' + str(new_proxy))
if new_list is new_weak_list:
    print("There is a weak reference")
print('The Number of Weak references: ' +
      str(weakref.getweakrefcount(new_list)))
del new_list, new_weak_list  # Delete both objects
print("The weak reference is: " + str(weak_ref()))
