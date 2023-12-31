meals_1 = ['redneck ribs','prawn star','san quentin squid',
           'fist full of pizza','honky tonk chicken']
meals_2 = ['redneck','prawn star','running bear salmon',
           'running bear salmon','honky tonk chicken']

def meal(ls):
    for i in range(len(ls)):
        for j in range(i +1 ,len(ls)):
            if ls[i]==ls[j]:
                return True
    return False


# Kiểm tra xem có phần tử trùng nhau trong list không
a = meal(meals_1)
b = meal(meals_2)

print(f'Bữa ăn 1 có phần tử trùng nhau không?',a)
print(f'Bữa ăn 2 có phần tử trùng nhau không?',b)