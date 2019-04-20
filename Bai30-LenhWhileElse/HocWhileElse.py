count = sum = 0
print("Nhập vào 5 số >=0. Để tính trung bình")
while count < 5:
    val: int = int(input("Nhập giá trị: "))
    if val < 0:
        print("Nhập sai quy tắc")
        break
    sum += val
    count += 1
else:
    print("Trung Bình =", sum / count)
