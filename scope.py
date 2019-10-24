#x = 25

#def my_func():

   # x = 50

    #return x

#print(x)

#print(my_func())


x = 25

def my_func():

    x = 50

    return x

#print(x)

#print(my_func())

my_func()

print (x)


#example 2

name = "kennedy"

def full():

    #name = "sammy"

    def hello():
        print ("hello "+ name)


    hello()

full()


x = 50

def func(x):
    print('x is:', x)

    x = 1000

    print ('local x changed to:',x)


func(x)
print(x)



x = 50

def func():
    global x
    x = 1000

print ('The function call, x is: ', x)
func()
print ('after function call, x is: ', x)

# Instead of using global

x = 50

def func():
    #global x
    x = 1000
    return x

print ('The function call, x is: ', x)
x = func()
print ('after function call, x is: ', x)