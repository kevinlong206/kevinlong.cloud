a = [5, 9, 2, 4, 7]
b = [3, 7, 1, 9 ,2]
c = [6, 8, 0, 5, 3]

maxs = map(lambda n: max(*n), zip(a, b, c))
print(list(maxs))