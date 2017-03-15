from utils.timeit import timeit

"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""

def fib(n):
    #Memoize all the fibonacci numbers 
    a, b = 0, 1
    while True:
        if a > n:
            return
        yield a
        a, b = b, a + b

@timeit
def even_fib(n):
    return sum(filter(lambda x: x % 2 == 0, fib(n)))

if __name__ == "__main__":
    result = even_fib(4000000)
    print("Number of even valued terms are: {}".format(result))
