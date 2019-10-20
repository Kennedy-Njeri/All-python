def Fun(*args):
    for arg in args:
        print arg


l = [1,2,3,4,5]


Fun(*l)



def Fu2(**kwargs):
    for kwarg in kwargs.items():
        print kwarg


Fu2(num=12,last="kennedy")



def Fun2(*args, **kwargs):
    for arg in args:
        print arg

    for item in kwargs.items():
        print item


Fun2(15, score=12, name="vincent", digits=1234)


def myFun(n):
    return lambda a: a * n

mydouble = myFun(2)

print (mydouble(2))