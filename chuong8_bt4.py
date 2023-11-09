import math

def tinh_dien_tich_tam_giac(a, b, c):
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

a = int(input("Nhập độ dài cạnh a: "))
b = int(input("Nhập độ dài cạnh b: "))
c = int(input("Nhập độ dài cạnh c: "))

dien_tich = tinh_dien_tich_tam_giac(a, b, c)
print("Diện tích của tam giác là:", dien_tich)
