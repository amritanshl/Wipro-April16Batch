import pytest
from conftest import Calculator, calc_instance
# def test_calculator_add():
#    assert calc_instance.add(3,2)==5
# def test_calculator_multiply():
#     assert calc_instance.multiply(3,2)==6


@pytest.mark.parametrize( 
        "a, b,expected",[
            (3,2,5),
            (-10,20,10),
            (0,0,0),
            (1.6,1.4,3.0),
            (33,44, 88)
            ])   
def test_calculator_add(calc_instance,a,b,expected):
#    assert calc_instance.add(3,2)==5
    assert calc_instance.add(a,b) == expected

def test_divide_by_zero (calc_instance):
    with pytest.raises(ZeroDivisionError):
        calc_instance.divide(10,0)
# def test_calculator_add():
#     calc = Calculator()
#     assert calc.add(3,2) ==5
# def test_calculator_multiply():
#     calc = Calculator()
#     assert calc.multiply(4,12) == 48