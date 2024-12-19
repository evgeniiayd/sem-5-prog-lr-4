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

