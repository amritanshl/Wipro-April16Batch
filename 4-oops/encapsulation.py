#car_speed
#_car_speed = 0
#__car_speed = 0

from pyexpat import model


class Car:
    def __init__(self, make, fuel):
        self.make = make
        self.__fuel = fuel
    
    @property
    def fuel(self):
        return self.__fuel
    

    @fuel.setter
    def fuel(self, amount):
        if amount < 0:
            print("Fuel amount cannot be negative.")
        else:
            self.__fuel = amount
# Create an instance of the Car class
car = Car("Toyota", 50)
# Access the fuel propertyprint(f"Initial fuel: {car.fuel} liters")
current_fuel = car.fuel
current_fuel = -20
car.fuel = current_fuel
# Update the fuel propertycar.fuel = 30
print(f"Updated fuel: {car.fuel} liters")