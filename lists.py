
#lists

#mylist = [1,2,3]

mylist = ['a','b','c','d','e','f']

#mylist = ['stringdcfgvhv', 1,2,3,34, True, 'absdgh', [1,2,3]]

#print (len(mylist))

#print(mylist[-1])

#print("Before reassignment:")

#print (mylist)

#mylist[0] = 'New item'

#print ("After reassignment: ")

#print (mylist)

#mylist.append('python')

#listtwo = ['x', 'y', 'z']

#mylist.extend(listtwo)

item = mylist.pop()

#item = mylist.push()

mylist.reverse()

print (mylist)


print (item)

#sort

list1 = [3,2,4,1,5,8,6,7]

list1.sort()

print (list1)

#indexing a nested list

list2 = [1,2, ['v', 'x', 'y', 'z']]

print(list2[2][0])



#list comprehension

matrix = [[1,2,3], [4,5,6], [7,8,9]]

first_col = [row[0] for row in matrix]

print (first_col)


