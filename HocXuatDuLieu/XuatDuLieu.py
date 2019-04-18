print("-" * 20)
print('{0}x^2+{1}x+{2}'.format(5, 2, 3))

print("{0:>11}".format("Obama"))
print("{0:>11}".format("Putin"))
print("{0:>11}".format("Donal Trump"))
print("{0:>11}".format("Kim"))

print("-" * 15)
print("{0:>2} {1:>11}".format("STT", "Giá trị"))
print("-" * 15)
for i in range(1, 11):
    print("{0:>2} {1:>11}".format(i, 10 ** (11 - i)))

print("-" * 15)
