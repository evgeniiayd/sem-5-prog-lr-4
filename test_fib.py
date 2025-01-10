import main
from comparison_to_fib import FibonacchiList as FB


def test_fib_1():
    gen = main.my_genn()
    assert gen.send(3) == [1, 1, 2], "Тривиальный случай n = 3, список [1, 1, 2]"


def test_fib_2():
    gen = main.my_genn()
    assert gen.send(5) == [1, 1, 2, 3, 5], "Пять первых членов ряда"


def test_zero_class():
    assert list(FB([0])) == [], "Возвращение пустого списка"


def test_negative_class():
    assert list(FB([-1, -2, -3])) == [], "Возвращение пустого списка"


def test_the_number_class():
    assert list(FB([144, 1, 29])) == [144, 1], "Возвращение самого последнего числа Фибоначчи"
