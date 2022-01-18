from functools import reduce
from operator import mul

def factorial(n):
    return reduce(mul, range(1, n + 1), 1)
print(factorial(5))
print(factorial(0))
print(factorial(1))
print(factorial(10))