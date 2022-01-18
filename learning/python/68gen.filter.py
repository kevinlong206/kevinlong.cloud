cubes = [x**3 for x in range(10)]
print(cubes)
odd_cubes1 = filter(lambda cube: cube % 2, cubes)
print(odd_cubes1)
for cube in odd_cubes1:
    print(cube)
odd_cubes2 = (cube for cube in cubes if cube % 2)
print(odd_cubes2)
for cube in odd_cubes2:
    print(cube)
