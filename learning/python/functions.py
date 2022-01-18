def gcd(a, b):
    #calculate the greatest common devisor or (a, b).
    while b != 0:
        a, b = b, a % b
    return a



print(gcd(50,10))
