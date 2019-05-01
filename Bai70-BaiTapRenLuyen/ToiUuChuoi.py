def toiuuchuoi(s: str):
    s = s.strip()
    l: list = s.split(" ")
    while "" in l:
        l.remove("")
    s = " ".join(l)
    return s


s = "   Nguyen    Vu   Bien    Thuy   "
print(toiuuchuoi(s))
