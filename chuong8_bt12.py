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
x = int(input("Nhập số x: "))

if is_prime(x):
    print(x, "là số nguyên tố")
else:
    print(x, "không là số nguyên tố")