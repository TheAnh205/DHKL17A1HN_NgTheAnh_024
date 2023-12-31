tuple = ('red','green','yellow','blue','black','while',
         'pink','orange','red','blue')

e = int(input('nhập số dương từ 0 -9 :'))
f  = int(input('nhập số âm từ -1 - -9 :'))
d  = str(input('nhập màu cần đếm số lần : '))
a = tuple[e]
b = tuple[-f]
c =tuple.count(d)
print('vị trí đứng thứ ',e,' theo chiều dương là :',a)
print('vị trí đứng thứ ',f,' theo chiều âm là',b)
print('số lần lặp của ',d,'là ',c,'lần')