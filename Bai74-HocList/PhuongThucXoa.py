lst = [113, 20, 30, 40, 25, 16, 27, 40]
# Xóa phần tử trong list, nếu không tìm thấy báo lỗi, nếu trùng xóa phần tử đầu tiên
lst.remove(20)
print(lst)
lst.remove(40)
print(lst)
del lst[0]
print(lst)
del lst[1:4]  # Xóa các phần tử bắt đầu từ vị trí số 1 đến vị trí số 4 (nhưng không bao gồm nó)
print(lst)
lst = [15, 10, 20, 18]
print(lst)
del lst[1], lst[2]
# Xóa phần tử ở vị trí số 1 của lst --> được lst mới
# Sau đó xóa phần tử ở vị trí thứ 2 của lst mới
print(lst)
