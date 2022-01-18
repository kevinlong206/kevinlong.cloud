x = [1, 2, 3]
def func(x):
    x[1] = 42 #this effects caller !
    x = 'something else' #points x to new string objects

func(x)
print(x)
