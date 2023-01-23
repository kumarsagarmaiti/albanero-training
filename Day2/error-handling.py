# We can handle exceptions in programs like:
import sys
while True:
    try:
        x = int(input("Please enter a number"))
        break
    except ValueError:
        print("Oops!")

# A try statement may have more than one except clause, to specify handlers for different exceptions.
# The try … except statement has an optional else clause, which, when present, must follow all except clauses. It is useful for code that must be executed if the try clause does not raise an exception. For example:
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
# The use of the else clause is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the try … except statement.

# The try statement has another optional clause which is intended to define clean-up actions that must be executed under all circumstances. For example:


try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

# Goodbye, world!
# KeyboardInterrupt
# Traceback (most recent call last):
# File "<stdin>", line 2, in <module>
# If a finally clause is present, the finally clause will execute as the last task before the try statement completes. The finally clause runs whether or not the try statement produces an exception.
