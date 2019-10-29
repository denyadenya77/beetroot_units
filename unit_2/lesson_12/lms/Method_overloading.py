# Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat, and make
# their own implementation of the method talk be different. For instance Dog’s can be to print ‘voff voff’, while
# Cat’s can be to print ‘meow’

class Animal:

    def voice(self):
        return 'voice'

class Dog(Animal):

    def voice(self):
        return 'voff voff'


class Cat(Animal):

    def voice(self):
        return 'meow'


cat = Cat()
dog = Dog()

print(cat.voice())
print(dog.voice())