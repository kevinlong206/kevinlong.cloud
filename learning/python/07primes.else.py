primes = []
upto = 100
for n in range(2, upto + 1):
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else:  # interesting using of else at the same level as for loop not the if statement
        primes.append(n)
print(primes)