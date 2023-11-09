a = eval(input("Nhập hệ số a: "))
b = eval(input("Nhập hệ số b: "))

if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a
    print("Nghiệm của phương trình: x =", x)