i: int = 1
while i <= 10:
    for j in range(2, 10):
        print("{0} *{1:>2} = {2:>2}".format(j, i, j * i), end=' '*3)
    i += 1
    print()
