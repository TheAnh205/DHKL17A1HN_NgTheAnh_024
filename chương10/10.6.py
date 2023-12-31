import math
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
if a == 0:
    if b==0:
        print("Phương trình vô nghiệm")   
    else:
        print("Phương trình có nghiệm duy nhất là:",-c/b)    
delta=pow(b,2)-4*a*c
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép là",-b/(2*a))
else:
    print("Phương trình có 2 nghiệm phân biệt là: x1 = ",(-b+math.sqrt(delta))/(2*a),"x2 = ",(-b-math.sqrt(delta))/(2*a))
 


