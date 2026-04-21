class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.__speed = speed  # Protected attribute
    
    @property
    def speed_display(self):
        return self.__speed

my_car11 = Car("Toyota", 120)
print(my_car11.speed_display)  # Accessing the protected attribute through a property method

my_car11.__speed = -130  # Modifying the protected attribute directly (not recommended)
print(my_car11.speed_display)  # Displaying the speed through the property method (will not change due to name mangling)
print("---------------------")
my_car = Car("Toyota", 120)
print(my_car.speed_display)  # Accessing the protected attribute through a property method
my_car._speed = 130  # Modifying the protected attribute directly (not recommended)
print(my_car.speed_display)  # Displaying the updated speed through the property method

class Car1:
    def __init__(self, brand, speed):
        self.brand = brand
        self._speed = speed  # Protected attribute
    
my_car1 = Car1("Honda", 150)
print(my_car1._speed)  # Accessing the protected attribute directly (not recommended)
my_car1._speed = -160  # Modifying the protected attribute directly (not recommended)

