from math import sqrt
mx = 10
legs = [(a, b, sqrt(a**2 +  b**2))
         for a in range(1,mx) for b in range(a, mx)]


print(legs)

legs = filter(lambda triple: triple[2].is_integer(), legs)
# this will make the third number in the tuples integer



legs = list(
    map(lambda triple: triple[:2] + (int(triple[2]), ),legs)
)

print(legs)