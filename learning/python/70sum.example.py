
# there is a list comprehension in this one
# but it the entire list needs to be created
# before sum can run on the list
s1 = sum([n**2 for n in range(10**6)])

# these are the same, s3 just has redunant parenthesis
# this is a generator expression

s2 = sum((n**2 for n in range (10**6)))
s3 = sum(n**2 for n in range(10**6))

print(s1)
print(s2)
print(s3)
