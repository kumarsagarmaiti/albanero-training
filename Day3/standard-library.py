import glob
print(glob.glob("*"))

import random
x=random.sample(range(200),15)
print(x)

from datetime import date
now=date.today()
birthday=date(1998,9,27)
age=now-birthday
print(age.days)


def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
print(doctest.testmod())