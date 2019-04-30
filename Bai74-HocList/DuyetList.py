from random import randrange

n = int(input("Mời bạn nhập số phần tử: "))
lst = [0] * n
for i in range(n):
    lst[i] = randrange(-100, 100)
print(type(lst), lst, "Len = ", len(lst))
print("Duyệt List theo Collection")
for x in lst:
    print(x,end="\t")
print()
print("Duyệt List theo Index")
for i in range(len(lst)):
    print("lst[{0}] = {1}".format(i, lst[i]), type(lst[i]))
print("Duyệt List theo Index Ngược")
for i in range(len(lst) - 1, -1, -1):
    print("lst[{0}] = {1}".format(i, lst[i]), type(lst[i]))
