def toiuuchuoi(s: str):
    s = s.strip()
    l: list = s.split(" ")
    while True:
        if "" in l:
            l.remove("")
        else:
            break
    s = " ".join(l)
    return s


s = "   Nguyen    Vu   Bien    Thuy   "
print(toiuuchuoi(s))
