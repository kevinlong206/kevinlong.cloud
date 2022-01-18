A = 100
ex1 = [A for A in range(5)]
print(A) # prints 100

ex2 = list(A for A in range(5))
print(A) # prints 100

ex3 = dict((A, 2 * A) for A in range(5))
print(A) # prints 100


# the for loop alters the variable A, the others above do not
s = 0
for A in range(5):
    s += A
print(A) #prints 4
