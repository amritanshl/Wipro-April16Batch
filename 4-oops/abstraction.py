from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def accelerate(self):
        """A vehicle should accelerate"""
        pass
    
    @abstractmethod
    def brake(self):
        """A vechicle should move"""

class Toyota(Vehicle):
    def accelerate(self):
        return super().accelerate()
    def brake(self):
        return super().brake()
my_car = Toyota()
my_car.accelerate()


#Class : what is the blueprint?
#Encapsulation: What should I hide under the hood?
#Inheritance: Can I reuse an old blueprint for this?
#Polymorphism: Can I use the same button for different task?
#Abstraction: How can I make this look simple to user?