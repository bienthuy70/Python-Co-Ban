print("Chương trình kiểm tra năm nhuần")

"""
Năm nhuần là năm:
 - Chia hết cho 4 nhưng không chia hết cho 100
 - Hoặc chia hết cho 400
"""
year = int(input("Vui lòng nhập vào một năm: "))
ketqua = "Nhuần" if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else "Không Nhuần"
print("Năm ", year, "là năm ", ketqua)
