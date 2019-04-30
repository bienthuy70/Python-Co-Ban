lst = [1, 2, 3]
print(lst)
lst.insert(0, 999)
print(lst)
lst.insert(4, 888)
print(lst)
lst.insert(2, 777)
print(lst)
lst.append(666)
print(lst)
# insert, append một list con
lst.append([333, 555])
print(lst)
for x in lst:
    if type(x) is not list:
        print(x, end="\t")
    else:
        print(" and", end=" ")
        for y in x:
            print(y, end="\t")
        print(" of list", x)
