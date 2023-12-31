import calendar
ngay=int(input("Nhập ngày: "))
thang=int(input("Nhập tháng: "))
nam=int(input("Nhập năm: "))
print("Ngày tháng năm vừa nhập: ",ngay,"-",thang,"-",nam)
if calendar.isleap(nam):
    print("Năm",nam,"là năm nhuận")
else:
    print("Năm",nam,"không là năm nhuận")
if calendar.weekday(nam,thang,ngay) == 0:
    print(ngay,"-",thang,"-",nam,"là thứ hai")
if calendar.weekday(nam,thang,ngay) == 1:
    print(ngay,"-",thang,"-",nam,"là thứ ba")
if calendar.weekday(nam,thang,ngay) == 2:
    print(ngay,"-",thang,"-",nam,"là thứ tư")
if calendar.weekday(nam,thang,ngay) == 3:
    print(ngay,"-",thang,"-",nam,"là thứ năm")
if calendar.weekday(nam,thang,ngay) == 4:
    print(ngay,"-",thang,"-",nam,"là thứ sáu")
if calendar.weekday(nam,thang,ngay) == 5:
    print(ngay,"-",thang,"-",nam,"là thứ bảy")
if calendar.weekday(nam,thang,ngay) == 6:
    print(ngay,"-",thang,"-",nam,"là chủ nhật")
a=str(calendar.monthrange(nam,thang))
b=a[4:6]
print("Số ngày trong tháng",thang,"là:",b)
