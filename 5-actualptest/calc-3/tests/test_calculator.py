import pytest
from src.calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()


@pytest.mark.parametrize("a, b, expected",
            [
            (3,2,5),
            (-10,20,10),
            (0,0,0),
            (1.6,1.4,3.0),
            (33,44, 88)
            ])   
def test_addition_variation(calc, a, b, expected):
    """
    Simple functional test for addition
    """
    assert calc.add(a,b)==expected

def test_multiplication_variation(calc, a, b, expected):
    """
    Simple functional test for multiplication
    """
    assert calc.multiply(a,b)==expected
def test_subtraction_variation(calc, a, b, expected):
    """
    Simple functional test for Subtraction
    """
    assert calc.add(a,b)==expected
def test_division_variation(calc, a, b, expected):
    """
    Simple functional test for multiplication
    """
    assert calc.add(a,b)==expected