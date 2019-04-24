import time

start = time.process_time()
x = int(input("Nhập x: "))
end = time.perf_counter()
print("Thời gian thực hiện:", end - start)
