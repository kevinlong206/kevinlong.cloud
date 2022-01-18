class Person():
    species = 'Human'

print(Person.species) # Human
Person.alive = True # added dynamically !
print(Person.alive) # true

man = Person()
print(man.species) # Human (inherited)
print(man.alive) # True (inherited)

Person.alive = False
print(man.alive) # False (inherited)
man.name = 'Darth'
man.surname = 'Vader'
print(man.name, man.surname)
