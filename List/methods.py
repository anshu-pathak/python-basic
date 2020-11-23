# append()	=> Adds an element at the end of the list


#  using append methods
#  single value
# fruits = ['apple', 'banana', 'cherry', 'mango']
# fruits.append("orange")
# print(fruits)


# append a new sets in python.
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)
# ['apple', 'banana', 'cherry', ['Ford', 'BMW', 'Volvo']]


# clear()	Removes all the elements from the list
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)

# copy()	Returns a copy of the list
fruits = ['apple', 'banana', 'cherry', 'orange','apple', 'apple', 'apple']
x = fruits.copy()
print(x)


# count()	Returns the number of elements with the specified value
print(fruits.count("apple"))

# extend()	Add the elements of a list (or any iterable), to the end of the current list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)

print(fruits)


points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)

# index()	Returns the index of the first element with the specified value
x = fruits.index("cherry")
print(x)

numbers = [4, 55, 64, 32, 16, 32]
x = numbers.index(32)
print(x)

# insert()	Adds an element at the specified position
fruits = ['apple', 'banana', 'cherry']

fruits.insert(0, "orange")
print(fruits)

# pop()	Removes the element at the specified position
fruits.pop(0)
print(fruits)

# remove()	Removes the item with the specified value
fruits.remove('apple')
print(fruits)

# reverse()	Reverses the order of the list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)
fruits = [1, 2, 3, 4, 7, 9, 0, 22]
fruits.reverse()
print(fruits)

# sort() Sorts the list .
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

# give the value of the nums in accending order.
nums = [1, 2, 3, 4, 7, 9, 0, 22, 0.0, 5.2, 50, 2.2]
nums.sort()
print(nums)

# give the value of the nums in descending order.
nums.sort(reverse=True)
print(nums)