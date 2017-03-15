from utils.timeit import timeit

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

@timeit
def three_and_five(n):
    return sum(filter(lambda x: x % 5 == 0 or x % 3 == 0, range(1, n)))


if __name__ == "__main__":
    total = three_and_five(1000)
    print("Sum of all multiples of 3 or 5 between below 1000 is {}".format(total))
