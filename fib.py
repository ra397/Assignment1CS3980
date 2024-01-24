#fib.py
from functools import lru_cache
import time
import matplotlib.pyplot as plt

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        curr_exec_time = end - start
        print(f"Finished in {curr_exec_time:0.4f}s: f({args[0]}) -> {result}")
        fib_inputs.append(args[0])
        execution_times.append(curr_exec_time)
        return result
    return wrapper

fib_inputs = []
execution_times = []

@lru_cache
@timer
def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    fib(100)
    plt.plot(fib_inputs, execution_times)
    plt.xlabel('n in fib(n)')
    plt.ylabel('Execution Time')
    plt.show()