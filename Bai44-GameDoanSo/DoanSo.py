from random import randrange
while True:
    auto = randrange(1, 101)
    solandoan = 0
    while solandoan < 7:
        solandoan += 1
        print("Đoán lần thứ", solandoan)
        sobandoan = int(input("Máy đoán [1..100], Nhập số bạn đoán: "))
        if sobandoan is auto:
            print("Chúc mừng, bạn đã đoán đúng. Số máy =", auto)
            break
        elif sobandoan > auto:
            print("Bạn đã doán sai, số máy < số bạn đoán")
        else:
            print("Bạn đã doán sai, số máy > số bạn đoán")
    else:
        print("-"*20)
        print("Game Over, Số máy =", auto)
    tieptuc=input("Chơi tiếp không (c/k): ")
    if tieptuc is "k":
        print("Cám ơn bạn đã chơi Game!")
        break