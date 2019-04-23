while True:
    n: int = int(input('Nhập 1 số nguyên dương: '))
    i: int
    for i in range(2, n):
        if n % i == 0:
            print(n, "không phải là số nguyên tố")
            break
    else:
        print(n, 'không là số nguyên tố') if n is 1 else print(n, 'là số nguyên tố')
    tieptuc = input("Tiếp tục (c/k): ")
    if tieptuc is 'k':
        break
print("Cám ơn bạn đã sử dụng chương trình!")
