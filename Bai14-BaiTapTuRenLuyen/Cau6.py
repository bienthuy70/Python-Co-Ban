"""
i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2 = 5.0
d3 = -0.5
(a) = i1 + (i2*i3) = 2 - (5 * 3) = 2 - 15 = -13
(b) = i1 * (i2 + i3) = 2 * (5 - 3) = 2 * 2 = 4
(c) = i1 / (i2 + i3) = 2 / (5 - 3) = 2 / 2 = 1
(d) = i1 // (i2 + i3) = 2 // (5 - 3) = 2 // 2 = 1
(e) = i1/i2 + i3 = 2 / 5 - 3 = 0.4 - 3 = -2.6
(f) = i1//i2 + i3 = 2 // 5 - 3 = 0 - 3 = -3
(g) = 3 + 4 - 5 / 3 =  7 - 1.67 = 5.33
(h) = 3 + 4 - 5 // 3 =  7 - 1 = 6
(i) = (3 + 4 - 5) / 3 =  2 / 3 = 0.67
(j) = (3 + 4 - 5) // 3 =  2 // 3 = 0
(k) = d1 + (d2 * d3) = 2.0 - 5.0 * 0.5 = 2.0 - 2.5 = -0.5
(l) = d1 + d2 * d3 = 2.0 - 5.0 * 0.5 = 2.0 - 2.5 = -0.5
(m) = d1 / d2 - d3 = 2.0 / 5.0 + 0.5 = 0.4 + 0.5 = 0.9
(n) = d1 / (d2 - d3) = 2.0 / (5.0 + 0.5) = 2.0 / 5.5 = 0.36
(o) = d1 + d2 + d3 / 3 = 2.0 + 5.0 - 0.5 / 3 = 7.0 - 0.17 = 6.83
(p) = (d1 + d2 + d3) / 3 = (2.0 + 5.0 - 0.5) / 3 = 6.5 / 3 = 2.17
(q) = d1 + d2 + (d3 / 3) = 2.0 + 5.0 - (0.5 / 3) = 7.0 - 0.17 = 6.83
(r) = 3 * (d1 + d2) * (d1 - d3) = 3 * (2.0 + 5.0) * (2.0 + 0.5) = 3 * 7.0 * 2.5 = 52.5
"""
i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2 = 5.0
d3 = -0.5

a = i1 + (i2 * i3)
if a == -13:
    print("a =", True)
else:
    print("a =", False)

b = i1 * (i2 + i3)
if b == 4:
    print("b =", True)
else:
    print("b =", False)

c = i1 / (i2 + i3)
if c == 1:
    print("c =", True)
else:
    print("c =", False)

d = i1 // (i2 + i3)
if d == 1:
    print("d =", True)
else:
    print("d =", False)

e = i1 / i2 + i3
if e == -2.6:
    print("e =", True)
else:
    print("e =", False)

f = i1 // i2 + i3
if f == -3:
    print("f =", True)
else:
    print("f =", False)

g = 3 + 4 - 5 / 3
if round(g, 2) == 5.33:
    print("g =", True)
else:
    print("g =", False)

h = 3 + 4 - 5 // 3
if h == 6:
    print("h =", True)
else:
    print("h =", False)

i = (3 + 4 - 5) / 3
if round(i, 2) == 0.67:
    print("i =", True)
else:
    print("i =", False)

j = (3 + 4 - 5) // 3
if j == 0:
    print("j =", True)
else:
    print("j =", False)

k = d1 + (d2 * d3)
if k == -0.5:
    print("k =", True)
else:
    print("k =", False)

l = d1 + d2 * d3
if l == -0.5:
    print("l =", True)
else:
    print("l =", False)

m = d1 / d2 - d3
if m == 0.9:
    print("m =", True)
else:
    print("m =", False)

n = d1 / (d2 - d3)
if round(n, 2) == 0.36:
    print("n =", True)
else:
    print("n =", False)

o = d1 + d2 + d3 / 3
if round(o, 2) == 6.83:
    print("o =", True)
else:
    print("o =", False)

p = (d1 + d2 + d3) / 3
if round(p,2) == 2.17:
    print("p =", True)
else:
    print("p =", False)

q = d1 + d2 + (d3 / 3)
if round(q,2) == 6.83:
    print("q =", True)
else:
    print("q =", False)

r = 3 * (d1 + d2) * (d1 - d3)
if r == 52.5:
    print("r =", True)
else:
    print("r =", False)
