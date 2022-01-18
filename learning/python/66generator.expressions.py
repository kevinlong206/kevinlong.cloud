
### to be typed into python terminal, doesnt print anything ..

cubes = [k**3 for k in range(10)] #regular list
cubes # “[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]”
type(cubes) # <class 'list'>
cubes_gen = (k**3 for k in range(10)) # create as generator
cubes_gen #<generator object ..
type(cubes_gen) #<class 'generator'> “[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]”
list(cubes_gen) # this will exhaust the generator
list(cubes_gen) # nothing for to give !
