def tinh_tien_thue_phong(loai_phong, so_dem):
    gia_phong = {
        1: 1260000,   # Standard
        2: 1550000,   # Superior Garden View
        3: 1830000,   # Superior Ocean View
        4: 1830000,   # Garden View Bungalow
        5: 2120000,   # Pool View Bungalow
        6: 2120000,   # Family Room
        7: 2540000,   # Beach Front Bungalow
        8: 4800000    # VIP Sea View
    }

    if so_dem >= 4:
        ti_le_giam = 0.3
    else:
        ti_le_giam = 0.25

    gia_phong_giam = gia_phong[loai_phong] - gia_phong[loai_phong] * ti_le_giam
    thanh_tien = gia_phong_giam * so_dem

    return thanh_tien

# Nhập loại phòng và số đêm từ người dùng
loai_phong = int(input("Nhập loại phòng (từ 1-8): "))
so_dem = int(input("Nhập số đêm: "))

# Tính tổng số tiền thuê phòng
thanh_tien = tinh_tien_thue_phong(loai_phong, so_dem)

# Xuất kết quả
print("Thành tiền =", thanh_tien, "VNĐ")