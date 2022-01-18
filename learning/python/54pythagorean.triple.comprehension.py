from math import sqrt

mx = 10
legs = [(a, b, sqrt(a**2 + b**2))
    for a in range(1, mx) for b in range(a, mx)]

# here we combine filter and map in one CLEAN list comprehension

legs = [(a, b, int(c)) for a, b, c in legs if c.is_integer()]

print(legs)

print("hello")

x=6

print('goodbye')