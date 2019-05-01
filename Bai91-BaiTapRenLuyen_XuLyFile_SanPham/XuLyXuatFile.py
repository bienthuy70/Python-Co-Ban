def DocFile(path):
    File = open(path, 'r', encoding='utf-8')
    print("-"*77)
    print("| {0:<10}| {1:<50}|{2:>10} |".format("Mã SP", "Tên SP", "Đơn Giá"))
    print("-"*77)
    for line in File:
        data = (line.strip()).split(';')
        print("| {0:<10}| {1:<50}|{2:>10} |".format(data[0], data[1], data[2]))
    File.close()
    print("-"*77)


DocFile("sanpham.txt")
lst=[]
lst.sort(key=)


# Sắp xếp theo theo đơn giá giảm dần