import pytest
from calculator import Calculator


def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5


def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2


def test_multiply():
    calc = Calculator()
    assert calc.multiply(4, 3) == 12


def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5


def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(1, 0)


def test_history_records_operations():
    calc = Calculator()
    calc.add(2, 3)
    calc.multiply(4, 5)
    assert calc.history() == [
        {"op": "add", "a": 2, "b": 3, "result": 5},
        {"op": "multiply", "a": 4, "b": 5, "result": 20},
    ]


def test_clear_history():
    calc = Calculator()
    calc.add(1, 1)
    calc.clear_history()
    assert calc.history() == []


def test_divide_by_zero_not_recorded():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(1, 0)
    assert calc.history() == []
