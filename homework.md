# Homework

## Exercise 1: Fibonacci Sequence

1. Write a class named `Fibonacci` such that the following code will print the (infinite) Fibonacci sequence starting with 0, 1:

    ```python
    for n in Fibonacci(f0=0, f1=1):
        print(n)
    ```

    The Fibonacci sequence is defined as follows:

    > f<sub>0</sub> = 0  
    > f<sub>1</sub> = 1  
    > f<sub>n</sub> = f<sub>n-1</sub> + f<sub>n-2</sub> for n > 1

    That is, each term after the first two is the sum of the previous two terms. The first two terms are usually taken to be 0 and 1, but you can pick any two integers. So the first ten terms are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

2. Add to `Fibonacci` a method `ref` that returns the n<sup>th</sup> number in the sequence:

    ```python
    from typing import Iterable, Iterator

    class Fibonacci(Iterable[int]):
        """Computes the Fibonacci sequence."""
        def ref(self, n: int) -> int:
            """Returns the n-th Fibonacci number."""
            pass

    ```

3. Implement the same Fibonacci sequence as a *generator* (a function that uses the `yield` keyword):

    ```python
    from typing import Iterable
   
    def fibonacci(f0=0, f1=1) -> Iterable[int]:
        """Generates the infinite Fibonacci sequence."""
    ```
