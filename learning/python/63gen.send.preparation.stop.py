stop = False
def counter(start=0):
    n = start
    while not stop:
        yield n
        n += 1

c = counter()
print(next(c)) # prints 0
print(next(c)) # prints 1
stop = True  # the author doesnt like this solution w/ external variable as code is scattered
print(next(c)) # raise StopIteration exception!
