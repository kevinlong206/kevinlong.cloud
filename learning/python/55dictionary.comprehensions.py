from string import ascii_lowercase
lettermap = dict((c, k) for k, c in enumerate(ascii_lowercase, 1))
print(lettermap)

# or another way to do the same thing

lettermap = {c: k for k, c in enumerate(ascii_lowercase, 1)}
print(lettermap)
