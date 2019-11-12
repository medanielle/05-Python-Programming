import random

# the Coin class simulates a coin that can be flipped

class Coin:

    # the __init__ method initalizes the sideup data attribute 'Heads'
    # everytime you call a class it's init method runs each time
    def __init__(self):
        # __ in front means it is private variable... aka users cant mess with it
        self.__sideup = 'Heads'

    # the toss method generates a random number in the range of 0 through 1. If hte number is 0 then side up is set to 'Heads' otherewise side up is set to 'Tails'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    # the get_sideup method returns the Value refereces by sideup

    def get_sideup(self):
        return self.__sideup

# the main function 
def main():
    # create an object from the coin class
    my_coin = Coin()
    # print(type(my_coin))

    # sideup attribute is not private, with out __ in front
    my_coin.__sideup = 'Tails'

    # display th eside of coin that is facing up
    print('this side is up: ', my_coin.get_sideup())

    # Toss the coin
    print('I am tossing the coin...')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())


    # display th eside of coin that is facing up
    print('this side is now up: ', my_coin.get_sideup())

#main()