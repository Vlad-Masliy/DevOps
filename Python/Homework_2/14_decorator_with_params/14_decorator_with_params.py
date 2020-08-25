from functools import wraps
from time import time


def timeit(threshold=0):
    def time_count(func):
        @wraps(func)
        def time_it(*args, **kwargs):
            start = float(round(time(), 3))
            try:
                return func(*args, **kwargs)
            finally:
                end = float(round(time() - start , 3)) 
                if end >= threshold :
                    print(f"Total execution time:{end} s")
        return time_it
    return time_count


@timeit(threshold=10)
def euler_1():
    euler = []
    for i in range(1, 100000001):
        if i % 3 == 0 or i % 5 == 0:
            euler.append(i)
    return sum(euler)


timeit(euler_1())
