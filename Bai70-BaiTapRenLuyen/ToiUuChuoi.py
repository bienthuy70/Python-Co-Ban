def ToiUuChuoi(s):
    s = s.strip()
    return s


s = "   Nguyen   Vu Bien   Thuy   "
s = s.strip()
x = s.split(" ")
while True:
    if "" in x:
        x.remove("")
    else:
        break
print(x)
s2 = " "
s2 = s2.join(x)
print(s2)
