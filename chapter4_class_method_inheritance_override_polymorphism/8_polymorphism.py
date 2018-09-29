#Polymorphism with function
'''
Polymorphism is an important feature of class definition in Python that is utilized
when you have commonly named methods across classes or subclasses.

This allows functions to use objects of any of these polymorphic classes
without needing to be aware of distinctions across the classes.
'''

'''
DB connections - multiple connections and need to retrieve data from different classes using db connections


'''
class Bear(object):
    def sound(self):
        print("Groarrr")

class Dog(object):
    def sound(self):
        print("Woof woof!")

def makeSound(animalType):
    animalType.sound()

bearObj = Bear()
dogObj = Dog()

makeSound(bearObj)
makeSound(dogObj)