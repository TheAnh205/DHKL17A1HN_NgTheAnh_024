list = []

while True:
 i = int(input('Tiếp tục nhập giá trị không ? 1:Có, 2: không :   '))
 if i==1:
     a = int(input('Nhập giá trị bạn muốn thêm vào danh sách: '))
     list.append(a)
 elif i ==0:
    break
print("List bạn vừa nhập là : ",list)
# tìm giá trị x trong list
x = int(input('NHập X đi iem yêu :'))
find = x in list
if find:
   print(x,'Có lặp trong dãy List ,số lần lặp của x là :',list.count(x))
else:
   print(x,'không xuất hiện trong dãy List')

# tìm coi phải max không
list1 =[]
if x == max(list):
   print(x,'Là number lớn nhất in List bạn vừa nhập')
else:
   for i in list:
      if i >x:
         list1.append(i)
print('danh sách các số lớn hơn ',x,'là',list1)
    
   
print('tổng các number trong list là :', sum(list))