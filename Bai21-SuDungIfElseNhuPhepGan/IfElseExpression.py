a = 5
b = 7
# Sử dụng If Else thông thường
if a != b:
    c = 115
else:
    c = 113
print(c)

# Sử dụng If Else như phép gán
c = 115 if a != b else 113
print(c)

x = int(input("Nhập 1 số: "))
print("Số Chẳn" if x % 2 == 0 else "Số Lẻ")
