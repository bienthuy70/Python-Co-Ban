# Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ
n = int(input("Nhập một số (có 1 đến 2 chữ số): "))
sodau = n // 10
socuoi = n % 10
chulot = "" if sodau <= 1 else "Mươi"

chudau = "" if sodau == 0 else "Mười" if sodau == 1 else "Hai" if sodau == 2 else "Ba" if sodau == 3 else "Bốn" \
    if sodau == 4 else "Năm" if sodau == 5 else "Sáu" if sodau == 6 else "Bảy" if sodau == 7 else "Tám" \
    if sodau == 8 else "Chín"

if socuoi == 0:
    chucuoi = "Không" if sodau == 0 else ""
elif socuoi == 1:
    chucuoi = "Một" if sodau <= 1 else "Mốt"
elif socuoi == 2:
    chucuoi = "Hai"
elif socuoi == 3:
    chucuoi = "Ba"
elif socuoi == 4:
    chucuoi = "Bốn"
elif socuoi == 5:
    chucuoi = "Năm" if sodau == 0 else "Lăm"
elif socuoi == 6:
    chucuoi = "Sáu"
elif socuoi == 7:
    chucuoi = "Bảy"
elif socuoi == 8:
    chucuoi = "Tám"
else:
    chucuoi = "Chín"

print("Số", n, "viết bằng chữ là:", chudau, chulot, chucuoi)
