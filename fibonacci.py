import operator
from itertools import islice
from math import sqrt
from typing import Iterator, Iterable, Callable, TypeVar


class Fibonacci(Iterable[int]):

    def __init__(self, fib0=0, fib1=1):
        self._seq = [fib0, fib1]

    def __str__(self):
        a, b = self._seq
        return f'fib({a}, {b})'

    def __repr__(self):
        return str(self)

    def __iter__(self):
        return FibonacciIterator(fib0=self._seq[0], fib1=self._seq[1])

    def __getitem__(self, item):
        if isinstance(item, int) and item >= 0:
            while len(self._seq) <= item:
                self._seq.append(self._seq[-1] + self._seq[-2])
            else:
                return self._seq[item]
        else:
            raise TypeError(f'Index should be a non-negative integer. Got {item}')


class FibonacciIterator(Iterator[int]):

    def __init__(self, fib0: int, fib1: int):
        self._a = fib0
        self._b = fib1
        self._k = 0

    def __str__(self):
        return f'fibonacci_iterator(index={self._k}, a={self._a}, b={self._b})'

    def __repr__(self):
        return str(self)

    def __next__(self) -> int:
        if self._k > 0:
            self._a, self._b = self._b, self._a + self._b
        self._k += 1
        return self._a


def fibonacci(a=0, b=1):
    yield a
    while True:
        a, b = b, a + b
        yield a


x = TypeVar('x')
y = ררררררררררררררר                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                TypeVar('y')
z = TypeVar('z')


def zipwith(op: Callable[[x, y], z], xs: Iterable[x], ys: Iterable[y]) -> Iterable[z]:
    return map(lambda xy: op(xy[0], xy[1]), zip(xs, ys))
44444

def flip(f: Callable[[x, y], z]) -> Callable[[y, x], z]:
    return lambda y, x: f(x, y)


if __name__ == '__main__':
    fib = Fibonacci()
    print(list(islice(fib, 0, 20)))
    print(f'fib[10] == {fib[10]}')
    # for k, ratio in enumerate(zipwith(operator.truediv,
    #                                   islice(fib, 2, 33),
    #                                   islice(fib, 1, 32))):
    #     print(f'[{k}] {1e12 * ratio:,.0f}')
    #
    # print(f'[phi] {1e12 * (1 + sqrt(5)) / 2:,.0f}')
