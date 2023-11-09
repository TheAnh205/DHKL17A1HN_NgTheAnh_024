def tinh_cuoc_taxi_7_cho(distance, waiting_time):
    if distance <= 30:
        cuoc_di_chuyen = 13000 * (distance / 0.8)
    else:
        cuoc_di_chuyen = 13000 * (30 / 0.8) + 14100 * (distance - 30)
    
    cuoc_cho = 0
    if waiting_time > 5:
        cuoc_cho = 800 * (waiting_time - 5)
    
    cuoc = cuoc_cho + cuoc_di_chuyen
    
    return cuoc_cho, cuoc_di_chuyen, cuoc


def tinh_cuoc_taxi_4_cho(distance,waiting_time):
    if distance <= 20:
        cuoc_di_chuyen = 11000 * (distance / 0.8)
    else:
        cuoc_di_chuyen = 11000 * (20 / 0.8) + 12100 * (distance - 20)
    
    cuoc_cho = 0
    if waiting_time >5:
        cuoc_cho = 800* (waiting_time - 5)
        cuoc= cuoc_cho + cuoc_di_chuyen
    return cuoc, cuoc_di_chuyen, cuoc

loai_xe = int(input("Nhập loại xe (4 chỗ - 1, 7 chỗ - 2): "))
distance = float(input("Nhập số km đã đi: "))
waiting_time = int(input("Nhập thời gian chờ (phút): "))

if loai_xe == 1:
    cuoc_cho, cuoc_di_chuyen, cuoc_taxi = tinh_cuoc_taxi_4_cho(distance, waiting_time)
elif loai_xe == 2:
    cuoc_cho, cuoc_di_chuyen, cuoc_taxi = tinh_cuoc_taxi_7_cho(distance, waiting_time)
else:
    print("Loại xe không hợp lệ")
    exit()

print("Tiền chờ:", cuoc_cho, "đồng")
print("Tiền di chuyển:", cuoc_di_chuyen, "đồng")
print("Tiền cước:", cuoc_taxi, "đồng")
