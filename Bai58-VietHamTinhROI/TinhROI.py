def ROI(doanthu, chiphi):
    return lambda dautu: ((doanthu - chiphi) / chiphi >= dautu)


dt, cp = eval(input("Nhập doanh thu, chi phí: "))
GoiYDauTu = ROI(dt, cp)
print("==> Nên Đầu Tư") if GoiYDauTu(0.75) else print("==> Khó Quá Bỏ Qua")
