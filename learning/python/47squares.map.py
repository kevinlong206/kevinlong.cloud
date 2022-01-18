# if you code like this you are not a Python guy! ;)
squares = []
for n in range(10):
    squares.append(n ** 2)

print(list(squares))


# this is better, one line, nice and readable
squares = map(lambda n: n**2, range(10))
print(list(squares))

