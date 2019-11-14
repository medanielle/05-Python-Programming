# holds genral data about Automobiles
class Automobile:
    #the init method accepts arguments for the make, model, mileage, and price. It initalizes the data attributes with these values.
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
    
    # the following methods are mutators for the class's data attributes
    def set_make(self, make):
        self.__make = make
    def set_model(self, model):
        self.__model = model
    def set_mileage(self, mileage):
        self.__mileage = mileage
    def set_price(self, price):
        self.__price = price

    # the following methods are accessors for the class's data attributes
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_mileage(self):
        return self.__mileage
    def get_price(self):
        return self.__price

# the Car class represents a cat . It is a subclass of the automobile class. (derived class)

class Car(Automobile):
    # the __init__ method accepts arguments for the car's make, model, mileage, price, and doors

    def __init__(self, make, model, mileage, price, doors):
        # Call the super classe's __init__ method and pass the required arguments.
        # Note that we also have to pass self as an argument
        super().__init__(make, model, mileage, price)  # could be Automobile.__init() **nut needs self in ()
        
        # initialize the doors attribute
        self.__doors = doors
    
    # method for the mutator (of doors)
    def set_doors(self, doors):
        self.__doors = doors

    # method for the accessor (of doors)
    def get_doors(self):
        return self.__doors

# the truck class represents a pickup truck.
# it is a subclass of the Automobile
class Truck(Automobile):
    #this method takes arguments for the make, model, mileage, price, and drive type
    def __init__(self, make, model, mileage, price, drive_type):
        # call the superclass's __init__ method and pass required arguments
        super().__init__(make, model, mileage, price)

        # intialize new attributes
        self.__drive_type = drive_type

    # method for the mutator (of drive_type)
    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type

    # method for the accessor (of drive_type)
    def get_drive_type(self):
        return self.__drive_type

# the SUV class represents a sport utility vehicle. It is a subclass for the Automobile class
class SUV(Automobile):
    #this method takes arguments for the make, model, mileage, price, and passanger capacity
    def __init__(self, make, model, mileage, price, pass_cap):
        # call the superclass's __init__ method and pass required arguments
        super().__init__(make, model, mileage, price)

        # intialize new attributes
        self.__pass_cap = pass_cap

    # method for the mutator (of pass_cap)
    def set_pass_cap(self,pass_cap):
        self.__pass_cap = pass_cap

    # method for the accessor (of pass_cap)
    def get_pass_cap(self):
        return self.__pass_cap
