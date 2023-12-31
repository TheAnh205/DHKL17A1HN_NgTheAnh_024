list = ['ant','bear','cat','dog','elephant','fish','goat','hippo','tigger','meal']

print('danh sách các con thú gồm : ',list)
a = str(input("nhập con thú cần tìm: "))
b = list.index(a)
print('con thú bạn cần tìm ở vị trí thứ ',b,'trong chuỗi các con thú')
print('số lương các con thú là',len(list))