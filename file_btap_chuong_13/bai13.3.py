# # mở đọc ghi file 

def mo_doc_ghi_file():
    name_file   =  input('nhập tên file :')
    with open(name_file,'w',encoding='utf-8') as f :
        f.write('Rain rain , go away; Come again another day ...')
    a  = open(name_file,'r',encoding='utf-8')
    print('nội dung của file là : ',a.read())

mo_doc_ghi_file()