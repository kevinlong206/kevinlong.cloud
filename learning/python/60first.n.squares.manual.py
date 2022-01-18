def get_squares_gen(n):
    for x in range(n):
        yield x ** 2

squares = get_squares_gen(4) # this creates a generator object
print(squares)# <generator object etc
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares)) # exhausted, so will raise exception
