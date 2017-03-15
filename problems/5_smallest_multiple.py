import fractions
from utils.timeit import timeit

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

@timeit
def smallest_multiple(n):
    expr = lambda a, b: a * b // fractions.gcd(a, b)
    return reduce(expr, range(1, n+1))

if __name__ == "__main__":
    result = smallest_multiple(20)
    print("The smallest positive number is: {}".format(result))
