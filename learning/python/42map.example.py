map(lambda *a: a, range(3))  # without wrapping in list...

list(map(lambda *a: a, range(3)))  # wrapping in list...

list(map(lambda *a: a, range(3), 'abc'))  # 2 iterables

list(map(lambda *a: a, range(3), 'abc', range(4, 7)))  # 3

# map stops at the shortest iterator
list(map(lambda *a: a, (), 'abc'))  # empty tuple is shortest

list(map(lambda *a: a, (1, 2), 'abc'))  # (1, 2) shortest

list(map(lambda *a: a, (1, 2, 3, 4), 'abc'))  # 'abc' shortest