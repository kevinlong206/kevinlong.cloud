def minimum(*n):
    print(n) # n is a tuple
    if n:
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)

minimum(1, 3, -7 ,9)  # n = (1, 3, -7, 9) - prints: -7
minimum()  #n = () - prints: nothing
