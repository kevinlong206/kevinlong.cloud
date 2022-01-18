def func():
    pass

func() #the return of this call won't be collected, its lost
a = func() # return value collected to a
print(a) #prints none