from functools import wraps
from time import time


def timeit(func):
    @wraps(func)
    def time_it(*args, **kwargs):
        start = float(round(time(), 3))
        try:
            return func(*args, **kwargs)
        finally:
            end = float(round(time()- start, 3)) 
            print(f"Total execution time: {end} s")

    return time_it


@timeit
def euler_1():
    euler = []
    for i in range(1, 100000001):
        if i % 3 == 0 or i % 5 == 0:
            euler.append(i)
    return sum(euler)


euler_1()
