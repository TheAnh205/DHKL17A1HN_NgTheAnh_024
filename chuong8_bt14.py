
N = int(input("Nhập số nguyên N: "))

S = 0

for i in range(N):
    num = int(input(f"Nhập số nguyên thứ {i+1}: "))
    S += num

print(f"Tổng {N} số nguyên bạn đã nhập là: {S}")

N = int(input("Nhập số nguyên N: "))

numbers = []
for i in range(N):
    num = int(input(f"Nhập số nguyên thứ {i+1}: "))
    numbers.append(num)

S = sum(numbers)

print(f"Tổng {N} số nguyên bạn đã nhập là: {S}")