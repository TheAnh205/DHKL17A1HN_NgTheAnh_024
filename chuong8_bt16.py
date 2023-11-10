def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

gcd = find_gcd(a, b)
print("Ước chung lớn nhất của", a, "và", b, "là:", gcd)