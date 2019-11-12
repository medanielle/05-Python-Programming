# this program imports the coin modile and created an instance of the coin class

import coinclass

def first():
    # create an onject from the coin class
    my_coin = coinclass.Coin()

    # Display the side that is facing up
    print('THis side is up', my_coin.get_sideup())

    # toss it 10 times
    print('I am tossing the coin...')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

#first


def second():
    # create the object from the coin class
    coin1 = coinclass.Coin()
    coin2 = coinclass.Coin()
    coin3 = coinclass.Coin()

    # Display the side of each coin that is facing up
    print('I have three coins with these sides up')
    print('Coin 1: ', coin1.get_sideup())
    print('Coin 2: ', coin2.get_sideup())
    print('Coin 3: ', coin3.get_sideup())

    # toss em
    print('I am tossing all three coins...\n')
    coin1.toss()
    coin2.toss()
    coin3.toss()
        
    # Display the side of each coin that is facing up
    print('I have three coins with these sides up')
    print('Coin 1: ', coin1.get_sideup())
    print('Coin 2: ', coin2.get_sideup())
    print('Coin 3: ', coin3.get_sideup())

#second()

# this program passes a coin object as an argument to a function
def coinArg():
    # create a coin object
    my_coin = coinclass.Coin()

    # this will display 'heads'
    print(my_coin.get_sideup())

    #flip
    flip(my_coin)

    # this will display flipped
    print(my_coin.get_sideup())

def flip(coin_obj):
    coin_obj.toss()

coinArg()
