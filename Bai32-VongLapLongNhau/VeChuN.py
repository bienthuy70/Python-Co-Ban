n = int(input("Nhập chiều cao: "))
for i in range(n):
    for j in range(n):
        if j is 0 or i is j or j is n - 1:
            print("*", end="")
        else:
            print(" ", end='')
    print()
