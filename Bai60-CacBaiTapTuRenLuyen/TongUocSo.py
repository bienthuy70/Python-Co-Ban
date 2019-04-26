def TongUocSo(n):
    tong = 0
    for i in range(1, n):
        if n % i is 0:
            tong += i
    return tong


def pefect():
    return lambda a: a is TongUocSo(a)


def abundant():
    return lambda a: a < TongUocSo(a)


sohoanthien = pefect()
sothinhvuong = abundant()
x = int(input("Nhập 1 số nguyên dương: "))
if sohoanthien(x):
    print(x,"là số hoàn thiện")
if sothinhvuong(x):
    print(x,"là số thịnh vượng")