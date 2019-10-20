cities = ['nairobi', 'kitale', 'kikuyu', 'kakamega', 'Nyeri']

#good way
#i = 0

#for city in cities:
    #print (i, city)
    #i +=1


for i, city in enumerate(cities):
    print (i, city)



#Step List


x_list = [1,2,3]

y_list = [2,4,4]

#for i in range(len(x_list)):
    #x = x_list[i]
    #y = y_list[i]
    #print (x,y)

#Better way

for x, y in zip(x_list, y_list):
    print (x, y)


#Swapping values/Tuple Unpacking

x = 10

y = -10

print ('Before: x= %d, y = %d' %(x, y))

#good way
#tmp = y

#y = x

#x = tmp

x, y = y, x

print ('After: x= %d, y = %d' %(x, y))


#Dictionaries

ages = {
    'Mary' : 27,
    'Jonayhan': 25,

    'Dick': 44
}

#if 'Dick' in ages:
    #age = ages['Dick']
    #print ('Dick is %s years old' % age)

#else:
    #age = 'Unknown'
    #print ('Dick is %s years old' % age)


#The Better Way
age = ages.get('Dick', 'Unknown')

print ('Dick is %s years old' % age)


#For Loop

needle = 'd'

haystack = ['a', 'b', 'c', 'd']

#found = False

for letter in haystack:
    if needle == letter:
        print ('Found')
#        found = True
        break
#if not found:
else:
    print ('Not Found')


#f = open('simple.txt')

#for line in f:


#text = f.read()

#for line in text.split("/n"):
    #print (line)

#f.close


#Better way

with open('simple.txt') as f:
    for line in f:
        print (line)









names = ['kennedy', 'Njeri']

x = reversed(names)

for name in x:
    print (name)


first = 'i am going to school'

for element in reversed(first):
    print (element)


#Reverse Algorithm

s = "My name is Kennedy"
words = s.split(' ')
string = []
for word in words:
    string.insert(0, word)

print("Reversed String:")
print(" ".join(string))


