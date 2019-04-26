def oscillate(a, b):
    x = []
    for i in range(a, b):
        x.append(i)
        x.append(-i)
    return x


for n in oscillate(-3, 12):
    print(n, end=' ')
print()
