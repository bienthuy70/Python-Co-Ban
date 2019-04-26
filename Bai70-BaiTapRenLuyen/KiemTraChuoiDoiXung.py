def CheckDoiXung(s):
    doixung = False
    lens = len(s)-1
    for i in range(lens+1):
        if s[i] != s[lens - i]:
            break
    else:
        doixung = True
    return doixung

while True:
    chuoi = input("Mời bạn nhập chuỗi: ")
    if CheckDoiXung(chuoi):
        print("Chuỗi đối xứng")
    else:
        print("Chuỗi không đối xứng")
    tieptuc = input("Tiếp tục không (c/k)? ")
    if tieptuc is "k":
        break
print("Cám ơn bạn đã sử dụng chương trình")
