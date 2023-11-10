S = 0
while True:
    try:
        num = int(input("Nhập số nguyên (kết thúc là số 0): "))
        
        if num == 0:
            break  
        
        S += num
    except ValueError:
        print("Lỗi: Không phải là số nguyên. Hãy thử lại.")


print("Tổng các số nguyên bạn đã nhập là:", S)