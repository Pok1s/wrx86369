import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 5) == -5

def test_multiply(calc):
    assert calc.multiply(4, 3) == 12
    assert calc.multiply(0, 100) == 0

def test_divide(calc):
    assert calc.divide(10, 2) == 5
    assert calc.divide(9, 3) == 3

def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(10, 0)

def test_power(calc):
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1

def test_add_empty(calc):
    with pytest.raises(TypeError):
        calc.add(None, 5)

def test_add_invalid_type(calc):
    with pytest.raises(TypeError):
        calc.add("two", 3)
        
def test_large_numbers(calc):
    assert calc.add(1e10, 1e10) == 2e10
    assert calc.multiply(1e5, 1e5) == 1e10

def test_zero_operations(calc):
    assert calc.add(0, 0) == 0
    assert calc.multiply(0, 5) == 0
    assert calc.power(0, 5) == 0

def test_negative_numbers(calc):
    assert calc.add(-5, -5) == -10
    assert calc.subtract(-5, 5) == -10
    assert calc.multiply(-2, 3) == -6