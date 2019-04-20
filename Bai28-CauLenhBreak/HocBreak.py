while True:
    x = int(input("Nhập vào 1 số: "))
    print(x, "là số chẳn" if x % 2 == 0 else "là sô lẻ")
    tieptuc = input("Bạn có muốn tiếp tục không (c/k): ")
    if tieptuc == "k":
        break
print("Bye! Cám ơn bạn đã sử dụng phần mềm này")
