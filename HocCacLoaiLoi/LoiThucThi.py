# Dùng try: except: để bắt lỗi phần mềm

try:
    x = 5
    y = 0
    z = x / y
    print(z)
except:
    print('Bị lỗi rồi!')

# Sau khi bắt lỗi, tiếp tục chạy phần mềm
print('Cám ơn bạn đã dùng phần mềm')