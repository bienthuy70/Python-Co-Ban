# Tính S = x + x^2/2! + x^3/3! + ... + x^n/n!
x = int(input("Nhập x: "))
n = int(input("Nhập n: "))
s = 0
i: int
giaithua: int = 1
for i in range(1, n + 1):
    giaithua *= i
    s += x ** i / giaithua
print("S({0},{1}) = {2}".format(x, n, s))
