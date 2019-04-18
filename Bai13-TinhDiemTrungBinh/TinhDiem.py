toan = float(input("{0:14}{1}".format("Nhập điểm Toán", ": ")))
ly = float(input("{0:14}{1}".format("Nhập điểm Lý", ": ")))
hoa = float(input("{0:14}{1}".format("Nhập điểm Hóa", ": ")))
dtb = (toan + ly + hoa) / 3
print("Điểm trung bình =", round(dtb, 2))
