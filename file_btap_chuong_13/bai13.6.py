import csv

def ghi_csv():
    name_file = input('Nhập tên file CSV: ')
    line_news = [] 

    while True:
        try:
            with open(name_file, 'a', newline='', encoding='utf-8') as file:
                dong = csv.writer(file)

                if line_news:
                    dong.writerow(line_news)
                    print('Dữ liệu đã được thêm vào tệp tin CSV.')
                    line_news = [] 

                print('Chọn hành động:  1. Nhập thêm nội dung  2. Kết thúc:')
                lua_chon = input()

                if lua_chon == '1':
                    line_new = input('Nhập dữ liệu muốn thêm vào CSV (các giá trị cách nhau bởi dấu phẩy): ')
                    line_news = line_new.split(',')

                elif lua_chon == '2':
                    print('Chương trình đã kết thúc.')
                    f = open(name_file)
                    a = f.read()
                    print('nội dung file là : ',a)
                    break

        except FileNotFoundError:
            print("File không tồn tại.")

ghi_csv()
