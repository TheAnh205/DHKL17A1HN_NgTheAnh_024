# mở đọc ghi vào cuối file 
def them_nd_append():
    name_file = input('Nhập tên tệp tin: ')

    while True:
        print('Chọn hành động:  1. Nhập thêm nội dung  2. In nội dung :')
        i = input()
        if i == '1':
            noi_dung_tep = input('Nhập nội dung: ')
            try:
                with open(name_file, 'a', encoding='utf-8') as f:
                    f.write('\n' + noi_dung_tep)
                print('Nội dung đã được thêm vào tệp tin.')
            except FileNotFoundError:
                print('Không tìm thấy tệp tin.')
        elif i == '2':
            try:
                with open(name_file, 'r', encoding='utf-8') as f:
                    print(f.read())
            except FileNotFoundError:
                print('Không tìm thấy tệp tin.')
            break
        
        else:
            print('Lựa chọn không hợp lệ. Vui lòng nhập lại.')

# Gọi hàm để thực hiện
them_nd_append()
