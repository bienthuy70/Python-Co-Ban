import math


def GiaiPhuongTrinhBac1(a, b):
    if a != 0:
        print("Phương Trình Có Một Nghiệm Duy Nhất x=", -b / a)
    else:
        if b == 0:
            print("Phương Trình Có Vô Số Nghiệm")
        else:
            print("Phương Trình Vô Nghiệm")


def GiaiPhuongTrinhBac2(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Phương trình Vô Nghiệm")
    elif delta == 0:
        print("Phương Trình Có Nghiệm Kép x1 = x2 =", -b / (2 * a))
    else:
        print("Phương Trình Có 2 Nghiệm Phân Biệt: x1 =", (-b + math.sqrt(delta)) / (2 * a)), "x2=", (
                -b - math.sqrt(delta))


print("Chương trình giải phương trình bậc 2")

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    GiaiPhuongTrinhBac1(b, c)
else:
    GiaiPhuongTrinhBac2(a, b, c)
