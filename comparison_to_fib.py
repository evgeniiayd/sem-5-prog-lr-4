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
