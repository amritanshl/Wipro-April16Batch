#polymorphism is the ability of an object to take on many forms. It allows us to use a single interface to represent different types of objects. In Python, polymorphism is achieved through method overriding and duck typing.

class Vehicle:
    def start_engine(self):
        print("Starting the engine...")
class PetrolCar(Vehicle):
    def start_engine(self):
        super().start_engine()
        print("Starting the petrol car engine...")

class ElectricCar(Vehicle):
    def start_engine(self):
        super().start_engine()
        print("Starting the electric car engine...")

class GeneralCar(Vehicle):
    def start_engine(self):
        print("Starting the general petrol car engine...")

class Tesla(GeneralCar):
    def start_engine(self):
        print("Starting the Tesla electric car engine...")
my_tesla = Tesla()
my_tesla.start_engine()