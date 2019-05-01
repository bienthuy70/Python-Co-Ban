from random import randrange


def TaoMaTran(m, n):
    lst = []
    [lst.append([randrange(0, 100) for j in range(n)]) for i in range(m)]
    return lst


m, n = eval(input("Nhập ma trận M (Dòng), N (Cột): "))
# Tạo và hiển thị List Đa chiều M dòng, N cột
lst = TaoMaTran(m, n)
[print("Dòng {0} -> {1}".format(i + 1, lst[i])) for i in range(len(lst))]
# Hiển thị dòng nhập từ bàn phím
x = int(input("Nhập dòng muốn hiển thị: "))
print(lst[x - 1])
# Hiển thị cột nhập từ bàn phím
x = int(input("Nhập cột muốn hiển thị: "))
[print(lst[i][x - 1]) for i in range(len(lst))]
# Tính GTLN
dongmax = [max(lst[i]) for i in range(len(lst))]
gtln = max(dongmax)
print("Giá trị lớn nhất của List[{0},{1}] = {2}".format(m, n, gtln))
