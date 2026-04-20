
#---Base class (Parent class)---
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def horn(self):
        return f"{self.brand} {self.model} says: Beep beep!"
#---Derived class (Child class)---
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)  # Call the constructor of the base class
        self.battery_capacity = battery_capacity
        
    def charge(self):
        return f"{self.brand} {self.model} is charging with a {self.battery_capacity} kWh battery."

basic_car = Car("Toyota", "Corolla")
electric_car = ElectricCar("Tesla", "Model S", 100)
print(basic_car.horn())  # Output: Toyota Corolla says: Beep beep!
print(electric_car.horn())  # Output: Tesla Model S says: Beep beep