def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    gcd = find_gcd(a, b)
    lcm = abs(a * b) // gcd
    return lcm

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

lcm = find_lcm(a, b)
print("Bội chung lớn nhất của", a, "và", b, "là:", lcm)