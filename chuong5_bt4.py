import math

a=int(input("Nhập cạnh tam giác thứ nhất:"));

b=int(input("Nhập cạnh tam giác thứ hai:"));

c=int(input("Nhập cạnh tam giác thứ ba:"));

cv=a+b+c

p=cv/2

dt=math.sqrt(p*(p-a)*(p-b)*(p-c))

print("Chu vi = ", cv)

print("Diện tích = ", dt)