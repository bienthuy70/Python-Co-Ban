"""
Tính diện tích tam giác theo công thức Herong:
cv = a + b + c
p = cv/2
dt = sqrt(p*(p-a)*(p-b)*(p-c))
"""
import math

a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))
if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("a =", a, "b =", b, "c =", c, "không thể là độ dài 3 cạnh tam giác")
else:
    p = (a + b + c) / 2
    dt = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("Diện tích tam giác =", dt)
