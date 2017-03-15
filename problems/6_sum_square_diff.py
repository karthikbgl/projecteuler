from utils.timeit import timeit

"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

@timeit
def sum_square_diff(n):
    squares = sum(map(lambda x: x * x, xrange(1, n+1)))
    sum_of_squares = sum(xrange(1, n+1)) ** 2
    return sum_of_squares - squares

if __name__ == "__main__":
    result = sum_square_diff(100)
    print("The difference between the sum of the squares are: {}".format(result))
