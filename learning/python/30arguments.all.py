def func(a, b, c=7, *args, **kwargs):
    print('a, b, c:', a, b, c)
    print('args:', args)
    print('kwargs:', kwargs)

func(1, 2, 3, *(5, 7, 9), **{'X': 'z', 'Z': 'z'})
func(1, 2, 3, 5, 7, 9, X='x', Z='z') # same as previous one
