import functools

list = [1, 2, 3, 4, 5, 6]

print ("The sum of the list elements is {}".format(reduce(lambda a, b: a + b, list)))

# lambda lambda arguments : expression
# A lambda operator can have any number of arguments but can have only one expression.

# def add(x, y):
 #   return x + y


# Call the function
# Output: 5

# print (add(2, 3))


# add = lambda x, y: x + y

# Output: 5
#print add(2, 3)


list1 = [2, 3, 5, 5]

subtract = (reduce(lambda x, y: x + y, list1))

print(subtract)


add = lambda x, y: x+y
print (add(2, 3))


# map map(function_object, iterable1, iterable2,...)


def multiply2(x):
    return x * 2


now = map(multiply2, [1, 2, 3, 4])
print (now)

# or

now1 = map(lambda x: x - 2, [1, 2, 3, 4, 5])

print (now1)