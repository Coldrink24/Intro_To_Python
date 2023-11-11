#Global - NonLocal


x = "global"
def outer():
    x = "local"
    print("outer1" ,x)
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner", x)

    inner()
    print("outer2",x)


outer()
print(x)

print("-----------------------")

y = "global"
def glo1():
    global y
    y = "local"
    print("glo11" ,y)

print(y)
glo1()
print(y)



