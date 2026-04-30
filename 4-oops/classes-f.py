
#blueprint for a Car class
class Car:
    wheels = 4
    def __init__(amrit, brand, model, year, color="Unknown"):
        amrit.brand = brand
        amrit.model = model
        amrit.year = year
        amrit.color = color

    def __str__(amrit):
        return f"{amrit.year} {amrit.brand} {amrit.model} {amrit.color}"
    
car1 = Car("Toyota", "Camry", 2020) #isntantiating the class
print(car1) 
car2 = Car("Honda", "Civic", 2019, "Blue")
print(car2.wheels)
# print(car2.color)
del car1
try:
    print(car1)  # This will raise an error since car1 has been deleted
except NameError:
    print("car1 has been deleted.")
#inheritance
class Vehicle:
    def horn(self):
        return "Beep beep!"
    
class Bike(Vehicle):
    def ring_bell(self):
        return "Ring ring!"
    

bike1 = Bike()
print(bike1.horn())
print(bike1.ring_bell())

#advnaced inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, year, color, battery_capacity):
        super().__init__(brand, model, year, color)
        self.battery_capacity = battery_capacity

    def __str__(self):
        return f"{super().__str__()} with a {self.battery_capacity} kWh battery"

electric_car1 = ElectricCar("Tesla", "Model 3", 2021, "White", 75)
print(electric_car1)

#Encapsulation
class Car1:
    def __init__(self):
        self.__engine_number = "12345ABC"  # Private attribute

    def get_engine_number(self):
        return self.__engine_number
    
    def drive(self):
        return "The car is driving."
car1 = Car1()
print(car1.get_engine_number())  # Accessing private attribute through a method
print(car1.drive())  # Using the drive method

#polymorphism
class PetrolCar(Car):
    def fuel_type(self):
        return "Petrol"

class ElectricCar(Car):
    def fuel_type(self):
        return "Electric"
petrol_car = PetrolCar("Ford", "Mustang", 2020, "Red")
electric_car = ElectricCar("Tesla", "Model S", 2021, "Black")
print(petrol_car.fuel_type())  # Output: Petrol
print(electric_car.fuel_type())  # Output: Electric

cars22 = [petrol_car, electric_car]
for car in cars22:
    print(f"{car} runs on {car.fuel_type()}.")

bmw = Car("BMW", "X5", 2022, "Silver")
print(bmw)
mecedes = Car("Mercedes", "C-Class", 2021, "Black")
print(mecedes)


class Car3:
    def __init__(self, brand, color):
        #using self to refer to the instance of the class
        self.brand = brand
        self.color = color

        #self must be the first parameter in the method definition, it refers to the instance of the class and allows us to access its attributes and methods
    def idenitify_car(self):
        return f"This is a {self.color} {self.brand}."
    
car3 = Car3("Audi", "Red")
car4 = Car3("Lexus", "Blue")
print(car3.idenitify_car())
print(car4.idenitify_car())
#Car3.idenitify_car(car3)  # This is equivalent to car3.idenitify_car()