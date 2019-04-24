from random import randrange

count = 0
while True:
    x = randrange(-100, 100)
    print(x) if x is 50 else print(x, end=',')
    count += 1
    if x == 50:
        break
print('Count =', count)
