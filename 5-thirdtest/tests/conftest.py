from src.calculator import Calculator
import pytest
@pytest.fixture(scope="function")
def calc_instance():
    return Calculator()