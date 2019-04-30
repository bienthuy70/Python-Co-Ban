lst = [0] * 12
item = 0
for i in range(len(lst)):
    item += 10
    lst[i] = item
print(lst)
print(lst[0:3])
print(lst[1:3])
print(lst[2::])
print(lst[::2])
print(lst[::3])
print(lst[::-1])
print(lst[-1])
print(lst[-len(lst)])
print(lst[-2])
print(lst[3])
for i in range(-1, -len(lst) - 1, -1):
    print(lst[i], end="\t")
print()
print(lst)
print(lst[2:-2:2])
