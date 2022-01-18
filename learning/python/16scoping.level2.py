def outer():
    test = 1 #outer scope

    def inner():
        test = 2 #innerscope
        print('inner:', test)
    inner()
    print('outer:', test)
test = 0 #globa scope
outer()
print('global: ', test)
