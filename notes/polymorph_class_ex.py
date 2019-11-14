# polymorphism

# polymorphism allows subclasses to have methods with the same names as methods in their super classes. It gives the ability for a program to call the correct method depending on te type of object that is used to call it

# sub class will overide the superclass

# the Mammal class represents a genericl mammal
class Mammal:
    # this method accepts argument for the mammal's species
    def __init__(self, species):
        self.__species = species

    # this methos displays a message indicating a mammal's species
    def show_species(self):
        print('I am a', self.__species)

    # this method is the mammal's way of making a generic sound
    def make_sound(self):
        print('Grrrr')

class Dog(Mammal):
    # this method calls the superclass's init method
    def __init__(self):
        super().__init__('Dog')
        # Mammal.__init__(self, 'Dog')

    # this method overides super class make_sound
    def make_sound(self):
        print('Woof! Woof!')

class Cat(Mammal):
    # this method calls the superclass's init method
    def __init__(self):
        Mammal.__init__(self, 'Cat')

    # this method overides super class make_sound
    def make_sound(self):
        print('Meow!')

# define main function
def main():
    mammal = Mammal('mammal')
    mammal.show_species()
    mammal.make_sound()

    cat = Cat()
    cat.show_species()
    cat.make_sound()

    dog = Dog()
    dog.show_species()
    dog.make_sound()

main()


# This program demos polymorphism

def example():
    mammal = Mammal('Regular Animal')
    mammal.show_species()
    mammal.make_sound()

    cat = Cat()
    cat.show_species()
    cat.make_sound()

    dog = Dog()
    dog.show_species()
    dog.make_sound()

    #display info
    print(f'Here are some animals and the sounds they make: \n--------------------------------------------\n')
    show_mammal_info(mammal)
    print()
    show_mammal_info('Dog')
    print()
    show_mammal_info(cat)
    print()

# the show_mammal_info function accepts an object as an argument, and calls its show_species and make_sound methods

def show_mammal_info(my_type):
    if isinstance(my_type, Mammal):    
        my_type.show_species()
        my_type.make_sound()
    else:
        print('That is not a Mammal!')

example()



# base class, iheitance, super class
# subclass or derived class = inheriting
# sllows the correct version of a method to be called within subclasses = polymorphis
# isinstance = 