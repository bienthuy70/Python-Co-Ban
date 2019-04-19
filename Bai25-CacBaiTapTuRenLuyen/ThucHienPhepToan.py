# Câu 5: Nhập vào 2 giá trị a, b và các phép toán "+", "-", "*", "/". Hãy xuất kết quả theo đúng phép toán đã nhập
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
x = input("Nhập phép toán (+, -, *, /): ")

if x == "+":
    print(a, x, b, "=", a + b)
elif x == "-":
    print(a, x, b, "=", a - b)
elif x == "*":
    print(a, x, b, "=", a * b)
elif x == "/":
    print(a, x, b, "=", a / b)
else:
    print("Phép toán không hợp lệ")
