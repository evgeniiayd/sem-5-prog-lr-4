# Лабораторная работа 4, Яблонская Евгения

Результат кода программы (первая строка - список, полученный с помощью функции; вторая - через класс; во втором списке числа Фибоначчи до десяти):
![image](https://github.com/user-attachments/assets/fc9cf632-c244-43ab-a374-3e757ac4404e)

Успешное прохождение тестов.
![image](https://github.com/user-attachments/assets/776ecec3-ebc2-45a7-ab11-d299ffc19a0e)

Код программы:
main.py
```
import functools
from comparison_to_fib import FibonacchiList


def fib_elem_gen():
    """Генератор, возвращающий элементы ряда Фибоначчи"""
    a = 0
    b = 1

    while True:
        yield b
        res = a + b
        a = b
        b = res


def my_genn():
    """Сопрограмма"""

    number_of_fib_elem = yield

    g = fib_elem_gen()
    lst: list = []

    for i in range(number_of_fib_elem):
        el = next(g)
        lst.append(el)

    print(f"{number_of_fib_elem}: {lst}")
    yield lst


def fib_coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        gen.send(None)
        return gen

    return inner


my_genn = fib_coroutine(my_genn)
gen_res = my_genn()
gen_res.send(5)

# enter = input('Введите лист: ').split(',')
# enter = [int(i) for i in enter]
enter = list(range(10))
print(list(FibonacchiList(enter)))
# [1, 1, 2, 3, 5, 8]
```

comparison_to_fib.py
```
class FibonacchiList:
    def __init__(self, instance):
        self.instance = instance
        self.idx = 0
        self.st_a = 0
        self.st_b = 1
        self.fib = [1]

    def __iter__(self):
        return self  # возвращает экземпляр класса, реализующего протокол итераторов

    def __next__(self): # возвращает следующий по порядку элемент итератора
        while True:
            try:
                exam = self.instance[self.idx] # получаем очередной элемент из iterable
                while self.st_b < exam:
                    prom = self.st_a + self.st_b
                    self.st_a = self.st_b
                    self.st_b = prom
                    self.fib.append(self.st_b)
                if exam in self.fib:
                    self.idx += 1
                    return exam

                self.idx += 1

            except IndexError:
                raise StopIteration
```

fib_test.py
```
import main
from comparison_to_fib import FibonacchiList as FB


def test_fib_1():
    gen = main.my_genn()
    assert gen.send(3) == [1, 1, 2], "Тривиальный случай n = 3, список [0, 1, 1]"


def test_fib_2():
    gen = main.my_genn()
    assert gen.send(5) == [1, 1, 2, 3, 5], "Пять первых членов ряда"


def test_zero_class():
    assert list(FB([0])) == [], "Возвращение пустого списка"


def test_negative_class():
    assert list(FB([-1, -2, -3])) == [], "Возвращение пустого списка"


def test_the_number_class():
    assert list(FB([144, 1, 29])) == [144, 1], "Возвращение самого последнего числа Фибоначчи"
```
