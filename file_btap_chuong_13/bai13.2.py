# mở đọc thống kê  đóng file


def thong_kefile():
    name_file =  input('nhập tên file ở đây ')
    try:
        with open(name_file,'r',encoding= 'utf-8') as f:
            read=  f.read()
            print('nội dung của file là : \n',read,'\n')
            so_dong = read.count('\n')
            print('số line của text là : ',so_dong)
            so_tu = len(read.split())
            print('số work = ',so_tu)
            so_ky_tu = len(read)
            print('số ký tự là : ',so_ky_tu)
    except FileNotFoundError:
        print('tệp tin k tồn tại ')

thong_kefile()