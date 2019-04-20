n = 15
s = 0
x: int
for x in range(1, n + 1, 2):
    if x is 3 or x is 11:
        continue
    s += x
print("S =", s)
