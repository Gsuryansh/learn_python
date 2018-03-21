"""Sometimes an object comes in many types or forms. If we have a button, there are many different draw outputs
(round button, check button, square button, button with image) but they do share the same logic: onClick().
We access them using the same method . This idea is called Polymorphism."""


""" Polymorphism with function """


class Bear(object):
    def sound(self):
        print "Groarrr"


class Dog(object):
    def sound(self):
        print "Woof woof!"


def makeSound(animalType):
    animalType.sound()


bearObj = Bear()
dogObj = Dog()

makeSound(bearObj)
makeSound(dogObj)

""" Here we have two class bear and dog both have same function sound() and we have a function outside of the class
called makesound which will take a object and call the function from the above two classes based on the function passed
 """


""" Pollymorphism with abstract class (Most Commonly Used) """

class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name
    def talk(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'

animals = [Cat('Missy'),
           Cat('Mr. Mistoffelees'),
           Dog('Lassie')]

for animal in animals:
    print animal.name + ': ' + animal.talk()

# prints the following:
#
# Missy: Meow!
# Mr. Mistoffelees: Meow!
# Lassie: Woof! Woof!

# So here method talk behave like polymorphically because it is defined in the Animal (parent) class bt not implimented so this is abstract method
#  this is implementd differently in child class so behave differently when call with different classes object.