from math import sqrt

xa, ya, xb, yb = eval(input("Nhập vào Tọa độ điểm A(xa,ya) và B(xb,yb): "))
print("A = ({0}, {1})".format(xa, ya))
print("B = ({0}, {1})".format(xb, yb))
AB = sqrt(pow(xb - xa, 2) + pow(yb - ya, 2))
print("Độ dài đoạn thẳng AB =", AB)
