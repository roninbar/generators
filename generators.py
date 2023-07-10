from typing import Iterable


# 1. Write a function that concatenates two lists. [a,b,c], [1,2,3] → [a,b,c,1,2,3]

def concat(xs: Iterable, ys: Iterable) -> Iterable:
    yield from xs
    yield from ys


# 2. Write a function that combines two lists by alternatingly taking elements,
#    e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].

def alternate(xs: Iterable, ys: Iterable) -> Iterable:

    x_stopped = y_stopped = False
    xit = iter(xs)
    yit = iter(ys)
    while not x_stopped or not y_stopped:
        try:
            yield next(xit)
        except StopIteration:
            x_stopped = True
        try:
            yield next(yit)
        except StopIteration:
            y_stopped = True


# 3. Write a function that merges two sorted lists into a new sorted list.
#    e.g. [1,4,6],[2,3,5] → [1,2,3,4,5,6]. You can do this quicker than concatenating them followed by a sort.

def merge(xs: Iterable[int], ys: Iterable[int]) -> Iterable[int]:
    pass


if __name__ == '__main__':
    for z in concat(['a', 'b', 'c', 'd', 'e'], [1, 2, 3]):
        print(z, end=' ')
