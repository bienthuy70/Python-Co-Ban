g = 5


def incrment():
    global g
    g = 2
    g = g + 1


incrment()
print(g)


def decrement():
    global x
    x = 2
    x = x - 1


decrement()
print("x =", x)
