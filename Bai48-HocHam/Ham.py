def ptb1(a, b):
    if a is 0 and b is 0:
        return "Phương trình có vô số nghiệm"
    elif a is 0 and b != 0:
        return "Phương trình vô nghiệm"
    else:
        return "Phương trình có một nghiệm duy nhất x = {0}".format(round(-b / a, 2))


def xuatdulieu(data):
    print(data)


kq1 = ptb1(0, 0)
kq2 = ptb1(0, 1)
kq3 = ptb1(6, 7)
print(kq1)
print(kq2)
print(kq3)
kq4=ptb1(3,7)
xuatdulieu(kq4)
