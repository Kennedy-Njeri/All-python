seq = [1, 2, 3, 4, 5, 6]

for item in seq:
    print(item)

d = {"ken": 23, "vincent": 24, "dan": 4}

for item in d:
    print (d)

mypairs = [(1, 5), (3, 4), (2, 3)]

for rent in mypairs:
    print (rent)

mypairs = [(1, 5), (3, 4), (2, 3)]

for (tup1, tup2) in mypairs:
    print (tup1)
    print (tup2)

# range

for item in range(10):
    print(item)

# list comprehension

x = [1, 2, 3, 4]

out = [num ** 2 for num in x]

print (out)

for i in range(1, 10):
    print i
