
def kiem_tra_nam_nhuan(nam):
    if (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0:
        return True
    else:
        return False

nam = int(input("Nhập vào năm kiểm tra: "))

if kiem_tra_nam_nhuan(nam):
    print(nam, "là năm nhuận")
else:
    print(nam, "không là năm nhuận")