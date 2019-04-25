'''
Nhập n. Tính S(n) = sqrt(2 + sqrt(2 + sqrt(2 + ... +sqrt(2)))), có n dấu căn
'''
from math import sqrt

n: int = int(input("Nhập n: "))
s = 0
for i in range(1, n + 1):
    s = sqrt(2+s)
print("S =", s)
