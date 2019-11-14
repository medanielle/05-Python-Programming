import inherit_class_ex 

#this program demos the Car Class
def car_demo():
    # create an onject from the Car class
    # the car is a 2007 Audi with 12,500 miles and $21,500.00 and has four doors
    used_car = inherit_class_ex.Car('Audi', 'A3', 12500, 21500.00, 4)

    # Display the cars Data
    print(f"Make: {used_car.get_make()}\nModel: {used_car.get_model()}\nMileage: {used_car.get_mileage()}\nPrice: ${used_car.get_price():,.2f}\nDoors: {used_car.get_doors()}")

#car_demo()

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
# this program creates a Car object and a SUV object
def car_truck_suv_demo():
    # create Car object
    car = inherit_class_ex.Car('Bugatti', 'Veyron', 0, 3000000, 2)

    truck = inherit_class_ex.Truck('Dodge', 'PowerWagon', 0, 57000, '4x4')

    suv = inherit_class_ex.SUV('Jeep', 'Wrangler', 200000, 5000, 4)

    # Display the cars Data
    print('VEHICLE INVENTORY\n==================')
    print(f"\nMake: {car.get_make()}\nModel: {car.get_model()}\nMileage: {car.get_mileage():,}\nPrice: ${car.get_price():,.2f}\nDoors: {car.get_doors()}")
    print(f"\nMake: {truck.get_make()}\nModel: {truck.get_model()}\nMileage: {truck.get_mileage():,}\nPrice: ${truck.get_price():,.2f}\nDrive Type: {truck.get_drive_type()}")
    print(f"\nMake: {suv.get_make()}\nModel: {suv.get_model()}\nMileage: {suv.get_mileage():,}\nPrice: ${suv.get_price():,.2f}\nPass Cap: {suv.get_pass_cap()}")
    
    # print(suv.__dict__)
    # OutPut =>  {'_Automobile__make': 'Jeep', '_Automobile__model': 'Wrangler', '_Automobile__mileage': 200000, '_Automobile__price': 5000, '_SUV__pass_cap': 4}

    # suv_dict = suv.__dict__
    # print(type(suv_dict))
    # OutPut =>  <class 'dict'>

    # print(isinstance(car, inherit_class_ex.Automobile))
    # OutPut =>  True
    # print(isinstance(car, inherit_class_ex.Truck))
    # OutPut =>  False
    # print(isinstance(car, inherit_class_ex.Car))
    # OutPut =>  True
    
    # print(issubclass(inherit_class_ex.SUV, inherit_class_ex.Automobile))
    # OutPut =>  True


car_truck_suv_demo()

# print(help(inherit_class_ex.SUV))

"""
class SUV(Automobile)
 |  SUV(make, model, mileage, price, pass_cap)
 |
 |  # the SUV class represents a sport utility vehicle. It is a subclass for the Automobile class
 |
 |  Method resolution order:
 |      SUV
 |      Automobile
 |      builtins.object
 |
 |  Methods defined here:
 |  
 |  __init__(self, make, model, mileage, price, pass_cap)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  get_pass_cap(self)
 |      # method for the accessor (of pass_cap)
 |  
 |  set_pass_cap(self, pass_cap)
 |      # method for the mutator (of pass_cap)
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Automobile:
 |
 |  get_make(self)
 |      # the following methods are accessors for the class's data attributes
 |
 |  get_mileage(self)
 |
 |  get_model(self)
 |
 |  get_price(self)
 |
 |  set_make(self, make)
 |      # the following methods are mutators for the class's data attributes
 |
 |  set_mileage(self, mileage)
 |
 |  set_model(self, model)
 |
 |  set_price(self, price)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Automobile:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 """




 