n = int(input("Nhập n: "))
s = 0
i: int
for i in range(1, n + 1):
    s += i
    if s >= 15:
        break
print("S =", s)
