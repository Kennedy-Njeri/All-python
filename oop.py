#class Dog():

    #Class Object Attribute

#    species = 'mammal'

#    def __init__(self,breed,name):
 #       self.breed = breed
  #      self.name = name

#myDog = Dog(breed='Bulldog',name='Huskie')

#print (myDog.breed)
#print (myDog.name)
#print (myDog.species)

class Circle():

    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius * Circle.pi

    def set_radius(self,new_r):
        self.radius = new_r


myCircle = Circle(3)

#print (myCircle.radius)

myCircle.set_radius(1000)

print (myCircle.area())