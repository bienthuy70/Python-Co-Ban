from time import sleep

n: int = int(input("Nhập chiều cao tam giác: "))
i: int
# Hình 1
print("Hình 1:")
print("-" * 6)
for i in range(1, 2 * n):
    j: int
    for j in range(1, 2 * n):
        print("*", end=' ') if (i <= n <= j < n + i) or (i >= n and (j <= 2 * n - i)) else print(" ", end=' ')
    print()
sleep(5)

# Hình 2
print('=' * 15)
print("Hình 2")
print("-" * 6)
for i in range(1, 2 * n):
    j: int
    for j in range(1, 2 * n):
        print("*", end=' ') if (n > i and (j is n or j is n + i - 1) or (n is i) or
                                (n < i and (j is 1 or j is 2 * n - i))) else print(" ", end=' ')
    print()
sleep(5)

# Hình 3
print('=' * 15)
print("Hình 3")
print("-" * 6)
for i in range(1, 2 * n):
    j: int
    for j in range(1, 2 * n):
        print("*", end=' ') if (i <= n <= j <= 2 * n - i) or (2 * n - i <= j <= n <= i) else print(" ", end=' ')
    print()
sleep(5)

# Hình 4
print('=' * 15)
print("Hình 4")
print("-" * 6)
for i in range(1, 2 * n):
    j: int
    for j in range(1, 2 * n):
        print("*", end=' ') if (i is 1 and j > n) or (j is n) or (j is 2 * n - i) or (i is 2 * n - 1 and j < n) \
            else print(" ", end=' ')
    print()
