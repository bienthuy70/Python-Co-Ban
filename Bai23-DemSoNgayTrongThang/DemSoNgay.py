print("Chương trình dếm số ngày trong tháng")
month = int(input("Nhập vào 1 tháng: "))
if month in (1, 3, 5, 7, 8, 10, 12):
    ketqua = 31
elif month in (4, 6, 9, 11):
    ketqua = 30
elif month == 2:
    year = int(input("Nhập vào 1 năm: "))
    ketqua = 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28
else:
    ketqua = 0
if ketqua == 0:
    print("Tháng không hợp lệ")
else:
    print("Tháng", month, "có", ketqua, "ngày")
