from random import randrange

lst = [0] * 10
for i in range(len(lst)):
    lst[i] = randrange(100)
print(lst)
lst.sort()
print(lst)
lst = [4, 2, 10, 8]
lst2 = sorted(lst)
print(lst)
print(lst2)
print("#" * 20)
lst = [8, 2, 10, 3]
print(lst)
lst.sort(reverse=True)
print(lst)
