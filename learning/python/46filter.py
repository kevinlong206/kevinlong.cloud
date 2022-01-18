test = [2, 5, 8, 0, 0, 1, 0]
list(filter(None, test))
list(filter(lambda: x: x, test)) # equivalent to previous

list(filter(lambda: x: x > 4, test) #keep only items < 4

