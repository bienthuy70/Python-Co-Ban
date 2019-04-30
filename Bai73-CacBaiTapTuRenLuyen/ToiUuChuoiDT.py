def ToiUuChuoiDT(s: str) -> str:
    s = s.strip()
    l: list = s.split(" ")
    s = ""
    item: str
    for item in l:
        if item != "":
            s += item.capitalize() + " "
    return s.strip()


s = "   nGuyeN    vU   biEn    ThuY   "
print(ToiUuChuoiDT(s))
