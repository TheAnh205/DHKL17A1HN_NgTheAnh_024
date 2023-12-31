import csv
# đọc tệp tin csv 
def read_csv():
        name_file =  input('nhập tên file csv vào đây :') # điển part1.csv
        f =open(name_file)
        list=[]
        for i in csv.reader(f):
            list.append(i)
        f.close()
        return list
print(read_csv())



