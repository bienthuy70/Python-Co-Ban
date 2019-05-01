lst = [12, 0, 25, 16]
print(lst)
lst.reverse()  # Thay đổi nội dung của lst
print(lst)
print("*" * 20)
lst = [8, 0, 2, 100, 20]
print(lst)
lst2 = reversed(lst)
print("Kiểu của lst2 =", type(lst2))
print(lst)
lst3 = list(lst.__reversed__())
print(lst)
print(lst2)
print(next(lst2))
print(lst3)
for item in lst2:
    print(item, end="\t")
print()

for item in lst3:
    print(item, end="\t")
print()
print(lst)

lst = ["Obama", 'Hahaha', "Ali33", """Kim Jong Un
Putin
Donal Trump"""]
print(lst)
lst.reverse()
print(lst)
