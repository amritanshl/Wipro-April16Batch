class Car:
    total_cars = 0
    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls, city):
        cls.factory_city = city
        return cls.total_cars

# Create instances of the Car class
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Mustang")
car4 = Car("Tesla", "Model 3")
car5 = Car("Chevrolet", "Impala")
# Access the class attribute
print(f"Total cars created: {Car.total_cars}")