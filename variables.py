x = "x is global variable"

def f():
    global x
    y = "y is local variable"
    print(x)
    print(y)

f()

print(x)
print(y)