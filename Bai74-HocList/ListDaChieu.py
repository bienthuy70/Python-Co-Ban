from random import randrange

lst = [[4, 2, 10], [7, 10, 5], [-7, 9, 2]]
print(lst)

for row in lst:
    for column in row:
        print(column, end="\t")
    print()
print("*" * 20)

for i in range(len(lst)):
    row = lst[i]
    for j in range(len(row)):
        print(row[j], end="\t")
    print()
print("*" * 20)

for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j], end="\t")
    print()

rowsize = int(input("Nhập số dòng: "))
columnsize = int(input("Nhập số cột: "))
arrdc = []
for i in range(rowsize):
    rowi = []
    for j in range(columnsize):
        rowi.append(randrange(-100, 100))
    arrdc.append(rowi)
print(arrdc)
print("*" * 20)
for i in range(len(arrdc)):
    for j in range(len(arrdc[i])):
        print(arrdc[i][j], end="\t")
    print()
