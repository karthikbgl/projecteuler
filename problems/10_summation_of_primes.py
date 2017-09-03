import math
from utils.timeit import timeit


"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

@timeit
def sum_of_primes(n):
    total = 2
    for i in xrange(3, n+1, 2):
        if filter(lambda j: i % j == 0, range(2, int(math.sqrt(i)))):
            continue
        total += i
    return total

if __name__ == "__main__":
    n = 2000000
    primes = sum_of_primes(n)
    print("Sum of primes is:  {}".format(primes))
