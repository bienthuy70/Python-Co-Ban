def TachDong(s: str):
    s = s.split(";")
    chan = sole = soam = sont = 0
    for i in s:
        if eval(i) % 2 == 0:
            chan += 1
        else:
            sole += 1
        if eval(i) < 0:
            soam += 1
        print(i)
    print("Số số chẳn:", chan)
    print("Số số lẻ:", sole)
    print("Số số âm:", soam)


s = "5;7;8;-2;8;11;13;9;10"
TachDong(s)
