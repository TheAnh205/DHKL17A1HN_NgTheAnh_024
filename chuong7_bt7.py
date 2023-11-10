so_tien = int(input("Nhập số tiền cần đổi: "))
menh_gia = [500000, 200000, 100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]
print("Số tiền cần đổi:", so_tien)
for mg in menh_gia:
  so_to = so_tien // mg
  if so_to > 0:
    print("Số tờ", mg,":", so_to)
    so_tien = so_tien - so_to * mg
    print("Tiền còn lại:", so_tien)