def is_perfect_number(x):
    if x <= 1:
        return False
    
    total = 1  # Khởi tạo tổng với ước số 1

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            total += i
            if i != x // i:
                total += x // i

    return total == x

x = int(input("Nhập số nguyên x: "))

if is_perfect_number(x):
    print(x, "là số hoàn hảo")
else:
    print(x, "không là số hoàn hảo")