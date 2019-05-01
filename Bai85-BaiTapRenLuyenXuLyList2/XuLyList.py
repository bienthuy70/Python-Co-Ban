# Viết lệnh khởi tạo ngẫu nhiên n phần tử cho list
from random import randrange

n = int(input("Nhập số phần tử: "))
lst = [randrange(0, 100) for i in range(n)]
print(lst)
k = int(input("Nhập số cần thêm: "))
lst.append(k)
print(lst)
k = int(input("Nhập phần tử muốn xóa: "))
while k in lst:
    lst.remove(k)
print(lst)


def CheckDoiXung(lst):
    lenlst = len(lst)
    for i in range(lenlst):
        if lst[i] is not lst[lenlst - i - 1]:
            return False
    return True


print("Chuỗi đối xứng") if CheckDoiXung(lst) else print("Chuỗi không đối xứng")
