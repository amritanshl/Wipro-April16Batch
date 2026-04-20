from abc import ABC, abstractmethod

class Calculator(ABC):
    @abstractmethod
    def calculate(self, a, b):
        """Every calculator must implement the calculate method."""
        pass
    
    def display_result(self, result):
        print(f"The result is: {result}")

class Adder(Calculator):
    def calculate(self,a,  b, c=100):
        
        result= a + b+c
        print(f"Adding {a} and {b} gives {result}")
        return result
    def display_result(self, result):        
        print(f"The sum is: {result}")

class Multiplier(Calculator):
    def calculate(self, a, b):
        result = a * b
        print(f"Multiplying {a} and {b} gives {result}")
        return result
class PowerCalculator(Calculator):
    def calculate(self, a, b):
        result = a ** b
        print(f"Raising {a} to the power of {b} gives {result}")
        return result
class PercentageCalculator(Calculator):
    def calculate(self, a, b):
        if b == 0:
            print("Cannot calculate percentage with a denominator of zero.")
            return None
        result = (a / b) * 100
        print(f"{a} is {result}% of {b}")
        return result
class sample (Calculator):
    pass

# Create instances of the calculators
adder = Adder() 
multiplier = Multiplier()
power_calculator = PowerCalculator()
percentage_calculator = PercentageCalculator()
# Perform calculations
adder.calculate(10, 5)
multiplier.calculate(10, 5)
power_calculator.calculate(2, 3)
percentage_calculator.calculate(50, 200)
# Attempting to create an instance of the abstract class will raise an error
try:        
    sample_calculator = sample()
    print("This will not be printed.")
except TypeError as e:
    print(f"Error: {e}")