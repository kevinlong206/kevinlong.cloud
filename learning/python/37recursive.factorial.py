def factorial(n):
    if n in (0,1): #base case
        return 1
    return factorial(n - 1) * n #recursive case


print(factorial(1))
print(factorial(2))
print(factorial(10))