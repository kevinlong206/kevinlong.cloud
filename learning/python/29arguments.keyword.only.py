def kwo(*a, c):
    print(a, c)

kwo(1, 2, 3, c=7)  #prints (1, 2, 3,) 7
kwo(c=4) #prints () 4

# kwo(1, 2)  #breaks,invalid syntax


def kwo2(a, b=42, *, c):
    print(a, b, c)

kwo2(3, b=7, c=99) #prints 3 7 99
kwo2(3, c=13) #prints 3 42 13