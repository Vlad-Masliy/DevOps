"""
These are different solutions of "Task 5: Multiples of 3 and 5. Find the best algorithm"

Let's find out which of the proposed algorithms is the most effective
"""

import multiprocessing
from functools import wraps
from time import time
import logging


logging.basicConfig(level=logging.INFO, format='')


N = 300000000


def timeit(func_name):
    def time_count(func):
        @wraps(func)
        def time_it(*args, **kwargs):
            start = time()
            try:
                return func(*args, **kwargs)
            finally:
                end = float(round(time() - start, 3))
                logging.info(f"{func_name} -> {end} sec")

        return time_it
    return time_count


@timeit('simple_iteration()')
def simple_iteration():
    res = 0
    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res


@timeit('several_for_loops()')
def several_for_loops():
    res = 0
    for i in range(3, N, 3):
        res += i
    for i in range(5, N, 5):
        res += i
    for i in range(15, N, 15):
        res -= i
    return res


@timeit('iterate_over_fifteen()')
def iterate_over_fifteen():
    range_diff = [0, 3, 5, 6, 9, 10, 12]
    res = 0
    for i in range(0, N, 15):
        for d in range_diff:
            v = i + d
            if v >= N:
                break
            res += v
    return res


@timeit('math_formula()')
def math_formula():
    upper = N - 1
    threes = int(3 * (upper / 3) * ((upper / 3) + 1) / 2)
    fives = int(5 * (upper / 5) * ((upper / 5) + 1) / 2)
    fifteens = int(15 * (upper / 15) * ((upper / 15) + 1) / 2)
    res = threes + fives - fifteens
    return res


def run_all_calculations_in_parallel():
    # Use multiprocessing library to run all above functions in parallel
    # Print execution time of each function
    proc1 = multiprocessing.Process(target=simple_iteration)
    proc1.start()
    proc2 = multiprocessing.Process(target=several_for_loops)
    proc2.start()
    proc3 = multiprocessing.Process(target=iterate_over_fifteen)
    proc3.start()
    proc4 = multiprocessing.Process(target=math_formula)
    proc4.start()
    proc1.join()
    proc2.join()
    proc3.join()
    proc4.join()


if __name__ == '__main__':
    run_all_calculations_in_parallel()
