
# mở đóng tệp tin 
def mo_tep_tin():
    name_file = input('nhập tên tệp tin :')
    try:
        with open(name_file,'r',encoding = 'utf-8') as f:
            print('nội dùng tệp tin là : \n',f.read())
    except FileNotFoundError:
        print('tệp tin k tồn tại ')

mo_tep_tin()# mở tệp tin HumptyDumpty.txt