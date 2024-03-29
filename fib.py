#fib.py
from functools import lru_cache
import time
import matplotlib.pyplot as plt

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter() # take the start time
        result = func(*args, **kwargs) # execute the function passed in and store the result
        end = time.perf_counter() # take the end time
        curr_exec_time = end - start # calculate the execution time
        print(f"Finished in {curr_exec_time:0.4f}s: fib({args[0]}) -> {result}") # print the execution time and the solution
        fib_inputs.append(args[0]) # append the input to inputs list, this will be the x-axis of our graph
        execution_times.append(curr_exec_time) # append the execution time of the input, this will be the y-axis of our graph
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
    # plot input vs execution time
    plt.plot(fib_inputs, execution_times)
    plt.title('Execution Times For Each Call of Fib(n)')
    plt.xlabel('n in fib(n)')
    plt.ylabel('Execution Time (seconds)')
    plt.show()