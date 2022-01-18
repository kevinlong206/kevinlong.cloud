def func(arg1, args2, ...):
    pass

func = deco1(deco2(func))

# is equivalent to the following:
@deco1
@deco2
def func(arg1, arg2, ...):
    pass


# decorators closes to the function are executed first, so bottom-up .



##########################


def func(arg1, arg2, ...):
    pass
func = decoarg(argA, argB)(func)

# is equivalent to the following:
@decoarg(argA, argB)
def func(arg1, arg2, ...):
    pass
