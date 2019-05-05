"""
- Viết Phần mềm Quản lý Sản phẩm
- Mỗi Danh Mục có: Mã, Tên; Một danh mục có nhiều sản phẩm
- Mỗi Sản Phẩm có: Mã, Tên, Đơn giá; Mỗi một sản phẩm thuộc về một danh mục
- Cho phép thêm mới, sửa, xóa, tiềm kiếm, sắp xếp, lưu và đọc Text File
"""
import mysql.connector


def ThemDanhMuc(val):
    print("Đang kết nối...")
    mydb = mysql.connector.connect(host='localhost', user='qlsp', passwd='khongco', database='qlsp')
    mycursor = mydb.cursor()
    print("Kết nối thành công!")
    sql = "INSERT INTO dmnhom (manhom, tennhom) VALUES (%s, %s)"
    print("Đang thêm...")
    mycursor.executemany(sql, val)
    mydb.commit()
    print("Đã thêm thành công", mycursor.rowcount, "mẫu tin")
    mydb.close()


print("Phần mềm Quản Lý Sản Phẩm")
print("Nhập danh mục nhóm sản phẩm")
val = []
while True:
    manhom = input("Nhập Mã Nhóm: ")
    tennhom = input("Nhập Tên Nhóm: ")
    val.append((manhom.strip(), tennhom.strip()))
    tieptuc = input("Tiếp tục (c/k)? ")
    if tieptuc is 'k':
        break
print(val)
ThemDanhMuc(val)
