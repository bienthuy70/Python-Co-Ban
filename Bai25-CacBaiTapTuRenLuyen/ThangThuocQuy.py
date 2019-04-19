# Nhập vào 1 tháng, xuất ra tháng đó thuộc Quý mấy
thang = int(input("Nhập vào 1 tháng (1 - 12): "))
qui = 1 if thang < 4 else 2 if thang < 7 else 3 if thang < 10 else 4
print("Tháng", thang, "Thuộc Quý", qui)
