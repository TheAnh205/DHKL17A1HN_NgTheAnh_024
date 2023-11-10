n = int(input("Nhập số nguyên n: "))
total = 0
for i in range(1, n + 1, 2):
    total += i
print("Tổng các số lẻ nhỏ hơn hoặc bằng", n, "là:", total)
total = 0
for i in range(2, n + 1, 2):
    total += i
print("Tổng các số chẵn nhỏ hơn hoặc bằng", n, "là:", total)
product = 1
for i in range(1, n + 1):
    product *= i
print("Tích của các số từ 1 đến", n, "là:", product)
product = 1
for i in range(1, n + 1):
    if i % 3 == 0:
        product *= i
print("Tích của các số chia hết cho 3 nhỏ hơn hoặc bằng", n, "là:", product)

# Hàm kiểm tra số nguyên tố
def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True
n = int(input("Nhập số nguyên n: "))
total = 0
for i in range(2, n + 1):
    if is_prime(i):
        total += i
print("Tổng các số nguyên tố nhỏ hơn hoặc bằng", n, "là:", total)


input_string = input("Nhập chuỗi số nguyên cách nhau bằng dấu phẩy: ")
numbers = input_string.split(',')
total = 0
for number in numbers:
    try:
        total += int(number)
    except ValueError:
        print("Lỗi: Không phải là số nguyên:", number)
print("Tổng các số trong chuỗi là:", total)