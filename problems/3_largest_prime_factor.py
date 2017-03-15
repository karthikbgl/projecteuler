import math
from utils.timeit import timeit

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def prime_factors(n):
    x = 2
    factors = set()
    while n > 1:
        while n % x == 0: 
            factors.add(x)
	    n /= x
        x += 1
    return factors

@timeit
def largest_prime(n):
    primes = prime_factors(n)
    print(list(primes))
    return max(primes)

if __name__ == "__main__":
    result = largest_prime(600851475143)
    print("Largest prime factor of 600851475143 is: {}".format(result))
