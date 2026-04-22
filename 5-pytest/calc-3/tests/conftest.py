import pytest
from src.calculator import Calculator

@pytest.fixture(scope="function")

def calc():
    """
    Fixutre provide clean calculator instance for every test.
    'scope=function' ensure memory is cleared b/w tests.
    """
    calculator_obj = Calculator()
    yield calculator_obj
    del calculator_obj