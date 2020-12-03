import numpy as np
a = np.array([1, 2, 3])
print(a)
print('\n')

b = np.array([[1, 3, 6], [2, 4, 8], [8, 4, 9]])
print(b)

# This array attribute returns a tuple consisting of array dimensions. It can also be used to resize the array.
print(b.shape)
print(b.size)  # number of elements in the array.
print('\n')

c = np.array([1, 2, 3, 4, 5], dtype=int)
print(c)
print(c.itemsize)
print(c.dtype.name)
print('\n')

# use to create a dianamic array.
d = np.arange(80).reshape(16, 5)
print(d)
print(type(d))


student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)

a = np.array([[1, 2, 3], [4, 5, 6]])
a.shape = (3, 2)  # resize the array.
print(a)

a.reshape(3, 2)  # reshape the array.
print(a)

b = np.arange(24)
print(b)

# a = np.arange(24)
b.ndim

# now reshape it

b = b.reshape(2, 4, 3)
# b.reshape(number of array, number of row, number of column)
print(b)

x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(x.itemsize)

x = np.array([1, 2, 3, 4, 5], dtype=np.float32)
print(x.itemsize)


x = np.array([1, 2, 3, 4, 5])
print(x.flags)

list = range(5)
it = iter(list)

# use iterator to create ndarray
x = np.fromiter(it, dtype=float)
print(x)


# start and stop parameters set
y = np.arange(10, 20, 2)
print(y)
