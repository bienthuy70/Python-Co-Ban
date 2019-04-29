def TachDong(s: str):
    l: list = s.split(";")
    chan = sole = soam = sont = 0
    for x in l:
        if eval(x) % 2 == 0:
            chan += 1
        else:
            sole += 1
        if eval(x) < 0:
            soam += 1
        print(x)

    print("Số số chẳn:", chan)
    print("Số số lẻ:", sole)
    print("Số số âm:", soam)


s = "5;7;8;-2;8;11;13;9;10"
TachDong(s)
