import math

x = float(input("Nhập vào một góc: "))
sinx = math.sin(math.radians(x))
cosx = math.cos(math.radians(x))
tanx = math.tan(math.radians(x))
cotx = 1 / tanx
print("sin({0}) = {1}".format(x, sinx))
print("cos({0}) = {1}".format(x, cosx))
print("tan({0}) = {1}".format(x, tanx))
print("cot({0}) = {1}".format(x, cotx))