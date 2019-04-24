x: int = int(input("Nhập x: "))
n: int = int(input("Nhập n: "))
mauso = 1
s = 0
for i in range(n + 1):
    tuso = x ** (2 * i + 1)
    if i is 0:
        mauso=1
    else:
        mauso *= (2*i) * (2*i + 1)
    s += (tuso / mauso)
print("S =", s)
