from utils.timeit import timeit

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

@timeit
def max_palindrome():
    max_palindrome = 0
    x, y = 1, 1
    a = 999
    while a >= 100:
        b = 999
        while b >= a:
            product = b * a
            if product > max_palindrome and str(product) == str(product)[::-1]:
                max_palindrome = product
                x, y = a, b
            b = b - 1
        a = a - 1
    return x, y, max_palindrome

if __name__ == "__main__":
    x, y, product = max_palindrome()
    print("The max palindrome for 3 digit numbers are: {} * {} = {}".format(x, y, product))
