def outer_fun():
    var1 ='40'
    def inner_fun():
        print(var1)
    def inner_fun2():
        print(var1)

    inner_fun()
    inner_fun2()

outer_fun()