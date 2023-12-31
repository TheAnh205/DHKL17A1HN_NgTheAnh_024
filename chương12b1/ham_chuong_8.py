def chuong8_bai1():
 a=float(input("nhập số a:"))
 b=float(input("nhập số b:"))
 c=float(input("nhập số c:"))
 d=float(input("nhập số d:")) 
 max=a
 if max<b:
    max=b
 if max<c:
    max=c
 if max<d:
    max=d
 print ("max =",max)
 min=a
 if min>b:
    min=b
 if min>c:
    min=c
 if min>d:
    min=d
 print("min =",min)

def chuong8_bai2():
 x=float(input("nhập x:"))
 if x <0:
    s=-x
    print("|",x,"|=",s)
 else:
    print("|",x,"|=",x)

def chuong8_bai3():
    a=float(input("nhập hệ số a:"))
    b=float(input("nhập hệ số b:"))
    print("phương trình bậc nhất:",a,"x +",b,"= 0")
    if a==0:
     print("phương tình vô nghiệm")
    else:
     s=-b/a
    print("x =",s)

def chuong8_bai4():
    a=float(input("giá trị cạnh thứ nhất:"))
    b=float(input("giá trị cạnh thứ hai:"))
    c=float(input("giá trị cạnh thứ ba:"))
    if (a+b)>c and (a+c)>b and (b+c)>a:
     print("đây là một tam giác")
     q=(a+b+c)/2
     import math
     s=math.sqrt(q*(q-a)*(q-b)*(q-c))
     print("diện tích tam giác =",s)
    else:
        print("đây không phải một tam giác")
        
def chuong8_bai5():
 a=int(input("nhập năm:"))
 if (a%400==0) or ((a%4==0) and (a%100!=0)):
    print("năm",a,"là năm nhuận")
 else:
    print("năm",a,"không phải năm nhuận")
    
def chuong8_bai6():
 a=int(input("loại xe:"))
 b=float(input("số km:"))
 c=int(input("thời gian chờ:"))
 if c<=5:
    q=0
    print("tiền chờ:miễn phí")
 else:
    q=(c-5)*800
    print("tiền chờ:",q,"đồng")
 if a==4:
     if b<=0.8:
         s=11000
     if b<=20 and b>=0.8:
         s=12100*b
     if b>=20:
         s=12100*20+(b-20)*10000
 if a==7:
     if b<=0.8:
         s=13000
     if b<=30 and b>=0.8:
         s=14100*b
     if b>=30:
         s=14100*30+(b-30)*12000
     print("tiền di chuyển",s,"đồng")
 r=q+s
 print("tiền cước:",r,"đồng")

def chuong8_bai7():
 a=int(input("nhập số điện:"))
 if a>400:
    s=1678*50+50*1734+100*2014+100*2536+100*2834+(a-400)*2927
 if a>300:
    s=1678*50+50*1734+100*2014+100*2536+(a-300)*2834
 if a>200:
    s=1678*50+50*1734+100*2014+(a-200)*2536
 if a>100:
    s=1678*50+50*1734+(a-100)*2014
 if a>50:
    s=1678*50+(a-50)*1734
 else:
    s=1678*a
 print("tiền điện:",s,"đồng")
 
def chuong8_bai8():
 phong1 = float(1260000) 
 phong2 = float(1550000)
 phong3 = float(1830000) 
 phong4 = float(1830000)
 phong5 = float(2120000) 
 phong6 = float(2120000)
 phong7 = float(2540000) 
 phong8 = float(4800000)
 so_phong=float(input("nhập loại phòng:"))
 so_dem=float(input("nhập số đêm:"))   
 if(so_phong == 1) :
        tien_phong_1_dem = phong1
 elif(so_phong == 2):
        tien_phong_1_dem = phong2
 elif(so_phong == 3):
        tien_phong_1_dem = phong3
 elif(so_phong == 4):
        tien_phong_1_dem = phong4
 elif(so_phong == 5):
        tien_phong_1_dem = phong5
 elif(so_phong == 6):
        tien_phong_1_dem = phong6
 elif(so_phong == 7):
        tien_phong_1_dem = phong7
 elif(so_phong == 8):
        tien_phong_1_dem = phong8    

 if (so_dem == 1):
        so_tien = tien_phong_1_dem * 1
 elif (so_dem >= 2 and so_dem <= 3):
        so_tien = tien_phong_1_dem * so_dem * 0.75
 else:
        so_tien = tien_phong_1_dem * so_dem * 0.7
 print("tổng số tiền phải trả:",so_tien)

def chuong8_bai9():
   a=int(input("nhập số n:"))
   while a>0:
    print(a)
    a-=1
   print("start!!!")

def chuong8_bai10():
   x=float(input("nhập x:"))
   n=int(input("nhập n:"))
   s=(x*x+1)**n
   print("S=(x*x+1)^n=",s)

def chuong8_bai11():
 x=float(input("nhập x:"))
 n=int(input("nhập n:"))
 s=(x*x +x+1)**n+(x*x-x+1)**n
 print("A=(x*x+x+1)^n+(x*x-x+1)^n=",s)

def chuong8_bai12():
 a=int(input("nhập số:"))
 t=0
 for i in range(2,a):
    if a%i==0:
        t=1
        print("đây là số nguyên tố")
        break
 if a==2:
  print("đây là số nguyên tố")
 else:
  print("đây không là số nguyên tố")
  
def chuong8_bai13():
 a=int(input("nhập số n:"))
 A=0
 B=0
 C=1
 D=1
 E=0
 F=0
 for i in range(1,a):
     if i%2!=0:
         A+=i
 print("A=",A)
 for i in range(1,a):
     if i%2==0:
        B+=i
 print("B=",B)     
 for i in range(1,a):
    if i%2!=0:
        C*=i
 print("C=",C)
 for i in range(1,a):
    if i%3==0:
        D*=i
 print("D=",D)
 for i in range(2,a):
    if a%i==0:
     E+=i
 print("E=",E)
 for i in range(1, a+1):
    if i%2!=0:
        F+=1/i
    elif i%2==0:
        F-=1/i
 print("F=",F)

def chuong8_bai14():
 a=int(input("nhập số nguyên thứ 1:"))
 b=int(input("nhập số nguyên thứ 2:"))
 c=int(input("nhập số nguyên thứ 3:"))
 S=a+b+c
 print(f"S = {S}")

def chuong8_bai15():
 a = 0
 while True:
    try:
        i = int(input("Nhập số nguyên (nhập 0 để kết thúc): "))
        if i == 0:
            break
        a += i
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")

 print("S=:", a)

def chuong8_bai16():
 a=int(input("nhập số a:"))
 b=int(input("nhập số b:"))
 r = a % b
 while r != 0:
        a = b
        b = r
        r = a % b
 print(b)

def chuong8_bai17():
 a=int(input("nhập số a:"))
 b=int(input("nhập số b:"))
 if a>b:
    for i in range(1,a+1):
        s=b*i
        if s%a==0 and s%b==0:
         print("BCNN=",s)         
         break
    c=(a*b)/s
    print("ƯCLN=",c) 
 if a<b:
    for i in range(1,b+1):
        s=a*i
        if s%a==0 and s%b==0:
         print("BCNN=",s)
         break
    c=(a*b)/s
    print("ƯCLN=",c) 
 if a==b:
    print("BCNN=1")
    print("ƯCLN=",a) 

def chuong8_bai18():
 a=int(input("nhập số:"))
 s=0
 for i in range(1,a):
    if a%i==0:
        s+=i
 if a==s:
    print(a,"là số hoàn hảo")
 else:
    print(a,"không là số hoàn hảo")

def chuong8_bai19():
 b=list(int(input("nhập dãy số:")))
 a = []
 for i in range(3):
    a = a + [int(input("Nhập phần tử thứ " + str(i) + ": "))]
 print(a)

def chuong8_bai20():
 import math
 x=int(input("Nhap x:"))
 ex=1
 n=1
 t=x
 while math.fabs(t)>=0.0001:
    ex +=t
    n +=1
    t *=(x/n)
 
 print("Gia tri gan dung cua e mu x la:",ex)
 