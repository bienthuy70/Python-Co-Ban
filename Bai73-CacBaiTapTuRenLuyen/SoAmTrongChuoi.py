def NegativeNumberInStrings(s: str):
    s = s.strip()
    l: list = s.split("-")
    s1: str
    print("Các số âm trong dãy số là:",end=" ")
    for s1 in l:
        strsoam = "-"
        for i in range(len(s1)):
            if s1[i].isnumeric():
                strsoam += s1[i]
            else:
                break
        if strsoam != "-":
            print(strsoam,end=" ")
    print()


s = "    Nguyen Vu -35 9 b-9a1  Bien--12T17thieu-89huy    "
NegativeNumberInStrings(s)
