def LuuFile(path, data):
    file = open(path, 'a', encoding='utf-8')
    file.writelines(data)
    file.writelines("\n")
    file.close()


print("Chương trình nhập thông tin sản phẩm")
while True:
    masp = input("Nhập Mã sản phẩm: ")
    tensp = input("Nhập Tên sản phẩm: ")
    dongia = float(input("Nhập đơn giá: "))
    # Lưu sản phẩm vào File
    row = "{0};{1};{2}".format(masp.strip(), tensp.strip(), dongia)
    LuuFile("sanpham.txt", row)
    tieptuc=input("Tiếp tục nhập liệu (c/k:)? ")
    if tieptuc is 'k':
        break
print("Cám ơn bạn đã sử dụng phần mềm.")

