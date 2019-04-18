import math

try:
    r = float(input("Mời bạn nhập bán kính đường tròn: "))
    cv = 2 * math.pi * r
    dt = r ** 2
    print("Chu vi =", round(cv, 2))
    print("Diện tích =", round(dt, 2))
except:
    print("Lỗi rồi!")
