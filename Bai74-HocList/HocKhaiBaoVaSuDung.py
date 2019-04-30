lst: list
lst = []
print(type(lst), lst, "Len =", len(lst))
lst = [3, -9, 8, 2, "5"]
print(type(lst), lst, "Len =", len(lst))
# Liệt kê các phần tử trong list theo Collection
item: str
for item in lst:
    print(type(item), item)
print("*" * 20)
# Liệt kê các phần tử theo chỉ số Index:
for i in range(len(lst)):
    print("lst[{0}] = {1}".format(i, lst[i]), type(lst[i]))
lst = [0.5] * 10
print(type(lst), lst, "Len =", len(lst))