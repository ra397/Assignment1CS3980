#fib.py
from functools import lru_cache


@lru_cache
def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    print(fib(100))