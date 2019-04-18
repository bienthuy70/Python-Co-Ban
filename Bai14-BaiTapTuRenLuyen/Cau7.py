"""
Hãy viết ngắn gọn các lệnh dưới đây:
(a) x=x+1 => x+=1
(b) x=x/2
(c) x=x-1
(d) x=x+y
(e) x=x-(y+7)
(f) x=2*x
(g) number_of_closed_cases=number_of_closed_cases+2*ncc
"""
x = 1
y = 2
number_of_closed_cases = 3
ncc = 4
print(x, y, number_of_closed_cases, ncc)
x += 1
print(x, y, number_of_closed_cases, ncc)
x /= 1
print(x, y, number_of_closed_cases, ncc)
x -= 1
print(x, y, number_of_closed_cases, ncc)
x += y
print(x, y, number_of_closed_cases, ncc)
x -= y + 7
print(x, y, number_of_closed_cases, ncc)
x *= 2
print(x, y, number_of_closed_cases, ncc)
number_of_closed_cases += 2 * ncc
print(x, y, number_of_closed_cases, ncc)
