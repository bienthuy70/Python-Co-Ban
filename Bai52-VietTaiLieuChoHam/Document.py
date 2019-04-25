def UocChungLonNhat(a, b):
    """Hàm này dùng để tìm ước số chung lớn nhất
    ví dụ: a = 9, b = 6 thì Ước SLN = 3
    :param a: Số thứ nhất
    :param b: Số thứ hai
    :return: Ước số chung lớn nhất của 2 số
    """
    min = a if a < b else b
    for i in range(min, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1


uoc = UocChungLonNhat(25, 15)
print(uoc)
