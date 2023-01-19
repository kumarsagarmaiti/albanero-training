# modules can be only imported from the same directory using file name like:
# import dummy
# dummy.fib(10)

# A module can contain executable statements or function definitions. These statements are used to initialize the module. They are executed the only the first time a module name is encountered in an import statement.
# The imported module names are placed in the importing module's global symbol table.

# We can also import all the available names(except those starting with _) from a module like:
# from dummy import *
# But this is generally not safe because it introduces unnecessary names in the module for the interpreter,possible hiding things that has already been defined in the module

# If the module name is followed by as, then the name following as is bound directly to the imported module.

# If the module name is followed by as, then the name following as is bound directly to the imported module.
# from dummy import fib as fibonacci

# When a module named spam is imported, the interpreter first searches for a built-in module with that name. If not found, it then searches for a file named spam.py in a list of directories given by the variable sys.path. sys.path is initialized from these locations:
# The directory containing the input script (or the current directory when no file is specified).
# PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
# The installation-dependent default.

# To speed up loading of the modules, Python caches the compiled version of each module in the folder __pycache__ under the name <module_name>.version.pyc where the version encodes the format of the compiled file; and it generally contains the python version number. This naming convention allows compiled modules from different releases and different versions to co-exist.
# Python checks the modification date of the source against the compiled version to see if it’s out of date and needs to be recompiled. This is a completely automatic process. Also, the compiled modules are platform-independent, so the same library can be shared among systems with different architectures.

# Python comes with a library of standard modules. Some modules are built into the interpreter; these provide access to operations that are not part of the core of the language but are nevertheless built in, either for efficiency or to provide access to operating system primitives such as system calls.

# The built-in function dir() is used to find which names a module defines. It returns a sorted list of strings. Without any arguments it returns the name of the current file. To get the names of built-in functions and variables builtins module is to be imported and passed in the dir function as an argument like this:
# import builtins
# dir(builtins)

# Packages are collections of modules and we can access modules inside them using the dot(.) notation.
# Note that when using from package import item, the item can be either a submodule (or subpackage) of the package, or some other name defined in the package, like a function, class or variable. The import statement first tests whether the item is defined in the package; if not, it assumes it is a module and attempts to load it. If it fails to find it, an ImportError exception is raised.

x = 'some'
y = 'this'


def foo(x):
    y = 'that'
    # print("My locals: ", locals())
    # print("My globals: ", globals())


# locals has x: other and y: that only
# globals contains x: some, y: this and many more global names
# foo('other')
# print(dir(foo))

import sys
# print(sys.path)
sys.path.append(r'C:\albanero\albanero-training\Day-1\intro.py')
print(globals()["__name__"])

from Day1.intro import cheeseshop

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch") 

print('heloo')
