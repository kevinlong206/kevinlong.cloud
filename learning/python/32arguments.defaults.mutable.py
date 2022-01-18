def func(a=[], b={}):
    print(a)
    print(b)
    print('#' * 12)
    a.append(len(a)) # this will affect a's default value
    b[len(a)] = len(a)

func()
func()
func()
func(a=[99, 99, 99], b={'B': 99})
func()
func()
func()
