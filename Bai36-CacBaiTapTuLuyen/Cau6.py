n: int = int(input("Nhập chiều cao: "))
# Hình vuông rỗng ruột
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print("*", end=' ') if i in (1, n) or j in (1, n) else print(" ", end=' ')
    print()

# Hình tam giác đặc ruột
print('-' * 15)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print("*", end=' ') if j > n - i else print(' ', end=' ')
    print()

# Hình tam giác đối xứng
print('-' * 15)
for i in range(1, 2 * n):
    for j in range(1, 2 * n):
        print("*", end=' ') if i is n or i is j or (j is 1 and i <= n) or (j is 2 * n - 1 and i >= n) \
            else print(' ', end=' ')
    print()
