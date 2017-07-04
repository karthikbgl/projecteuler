from utils.timeit import timeit

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def is_square(n):
    return (n ** 0.5) == int(n ** 0.5)

@timeit
def pythagorean_triplet(n):
    for i in range(1, n):
	for j in range(i+1, n):
            k = n - i - j
            if i ** 2 + j ** 2 == k ** 2:
                return i * j * k
    return 0

if __name__ == "__main__":
    n = 1000
    prod = pythagorean_triplet(n)
    print("The pythagorean product is {}".format(prod))
