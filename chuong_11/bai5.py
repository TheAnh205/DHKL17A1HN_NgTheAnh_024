list_numbers2 = []

while True:
 i = int(input('Tiếp tục nhập giá trị không ? 1:Có, 2: không :   '))
 if i==1:
     a = int(input('Nhập giá trị bạn muốn thêm vào danh sách: '))
     list_numbers2.append(a)
 elif i ==0:
    break
print("List bạn vừa nhập là : ",list_numbers2)

# tìm số nguyên tố trong list
list_nguyen_to =[]

for a in list_numbers2:
   if a < 2 :
      continue
   nt = True
   for i in range(2,a+1):
      if a % i ==0:
         nt = False
         break
      if nt:
        list_nguyen_to.append(a)

print('Danh sách các số nguyên tố trong list_numbers2 là : ',list_nguyen_to)


