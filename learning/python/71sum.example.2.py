#s = sum([n ** 2 for n in range(10**8)])
# ^ that could be killed on some systems, huge memory consumption

# this will succeed, memory optimized
s = sum(n**2 for n in range(10 ** 8))

print(s)
