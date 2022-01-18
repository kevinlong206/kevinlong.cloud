class Point():
    x = 10
    y = 7

p = Point()
print(p.x) # 10 (from class attribute)
print(p.y) # 7 from calass attribute

p.x = 12 # p get its own x attribute
print(p.x) #12 (now found in the instance)
print(Point.x) #10 (class attribute still the same)

del p.x # we delete the instance attribute
print(p.x) # now search has to again to find the class attribute

p.z = 3 # lets make a 3D Point
print(p.z) # 3

print(Point.z) # AttributeError: type object 'Point' has to attrib 'z'
