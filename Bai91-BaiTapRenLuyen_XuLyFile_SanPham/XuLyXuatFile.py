# Đọc File Lưu vào List
def FileToList(path: str, index: int = 2) -> list:
    File = open(path, 'r', encoding='utf-8')
    lst = []
    for line in File:
        data = line.strip().split(';')
        data[index] = float(data[index])
        lst.append(data)
    return lst


def RecordSort(lst: list, index: int = 0, mode: int = 0):
    for i in range(len(lst)):
        for j in range(len(lst)):
            a = lst[i]
            b = lst[j]
            if mode is 0:
                if a[index] < b[index]:
                    lst[i] = b
                    lst[j] = a
            else:
                if a[index] > b[index]:
                    lst[i] = b
                    lst[j] = a


# Sắp xếp theo theo đơn giá giảm dần
lst = FileToList("sanpham.txt")
print(lst)
RecordSort(lst, 2, 1)
print(lst)
