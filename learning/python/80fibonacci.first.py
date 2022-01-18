def fibonacci(N):
    # return all fib numbers up to N.
    result = [0]
    next_n = 1
    while next_n <= N:
        result.append(next_n)
        next_n = sum(result[-2:])
    return result

print(fibonacci(0)) #[0]
print(fibonacci(1)) # [0, 1, 1]
print(fibonacci(50)) # [ you get the idea]
