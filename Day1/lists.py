# Methods on list
# list.append(x)

# list.extend(iterable):Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
# original_list = [1, 2, 3]
# new_items = [4, 5, 6]
# original_list.extend(new_items)
# print(original_list)
# Output: [1, 2, 3, 4, 5, 6]

# list.insert(i, x):Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

# list.remove(x):Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

# list.pop([i]):Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.

# list.clear():Remove all items from the list. Equivalent to del a[:].

# list.index(x[, start[, end]]):Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.
# my_list = [1, 2, 3, 4, 5, 3, 6]
# my_list.index(3, 3, 7)
# 5


# list.count(x):Return the number of times x appears in the list.

# list.sort(key=None, reverse=False):Sort the items of the list in place.

# list.reverse():Reverse the elements of the list in place.

# list.copy():Return a shallow copy of the list. Equivalent to a[:].

from collections import deque

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
# 'Eric'
queue.popleft()
# 'John'
print(queue)
# deque(['Michael', 'Terry', 'Graham'])

# List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.
# squares = [x**2 for x in range(10)]
# [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec for num in elem]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# new=[[row[i] for row in matrix] for i in range(4)]
new=[[row[i] for i in range(4) ] for row in matrix]
print(new)

# There is a way to remove an item from a list given its index instead of its value: the del statement. This differs from the pop() method which returns a value. The del statement can also be used to remove slices from a list or clear the entire list.
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
# [1, 66.25, 333, 333, 1234.5]
del a[2:4]
# [1, 66.25, 1234.5]
del a[:]
# []
