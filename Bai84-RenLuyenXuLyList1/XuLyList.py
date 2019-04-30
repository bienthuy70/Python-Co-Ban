from random import randrange

# Khởi tạo list
n = int(input("Nhập số phần tử: "))
lst = [0] * n
for i in range(n):
    lst[i] = randrange(-100, 100)
print(lst)

# Thêm phần tử vào list
value = int(input("Nhập phần tử muốn thêm vào list: "))
lst.append(value)
print(lst)

# Đếm số phần tử xuất hiện trong list
k = int(input("Bạn muốn đếm số nào: "))
print("Số lần {0} xuất hiện trong list: {1}".format(k, lst.count(k)))


def CheckPrime(n):
    songuyento = False
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            songuyento = True
    return songuyento


dem = tong = 0
lstnt = []
for x in lst:
    if CheckPrime(x):
        dem += 1
        tong += x
        lstnt.append(x)
print("Có {0} số nguyên tố {1}. Tổng = {2}".format(dem, lstnt, tong))
print(lst)
lst.sort()
print("List sau khi sort", lst)