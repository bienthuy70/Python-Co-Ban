# Câu 4: Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày vừa nhập
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

# Số ngày trong tháng
if month in (1, 3, 5, 7, 8, 10, 12):
    daymax = 31
elif month in (4, 6, 9, 11):
    daymax = 30
elif month == 2:
    daymax = 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28
else:
    print("Tháng không hợp lệ")
    exit()

# Ngày kế tiếp
if day < daymax:
    daynext = day + 1
elif day == daymax:
    daynext = 1
else:
    print("Ngày không hợp lệ")
    exit()

# Tháng của ngày kế tiếp
if daynext > 1:
    monthnext = month
else:
    monthnext = month + 1

# Năm của ngày kế tiếp
if monthnext > 12:
    monthnext = 1
    yearnext = year + 1
else:
    yearnext = year

# Hiển thị ngày kế tiếp
print("Ngày kế sau ngày",day,"/",month,"/",year,"là ngày:",daynext,"/",monthnext,"/",yearnext)