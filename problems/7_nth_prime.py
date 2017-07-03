from utils.timeit import timeit

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def is_prime(x):
    if x == 2:
        return True
    for number in range (3, x): 
        if x % number == 0:
            return False
    return True

@timeit
def num_prime(n):
    lst = [2]
    for i in range(3, 10001**2, 2):
        if is_prime(i):
            lst.append(i)
            if len(lst) == n:
                return i

if __name__ == "__main__":
    n = 10001
    result = num_prime(n)
    print("The {}th prime is {}".format(n, result))
