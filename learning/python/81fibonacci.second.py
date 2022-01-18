def fibonacci(N):
    # return all fib numbres up to N
    yield 0
    if N == 0:
        return
    a = 0
    b = 1
    while b <= N:
        yield b
        a, b = b, a + b

print(list(fibonacci(0)))
print(list(fibonacci(1)))
print(list(fibonacci(50)))
