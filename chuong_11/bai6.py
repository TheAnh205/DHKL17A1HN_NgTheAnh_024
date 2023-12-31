height_inch =[74,74,72,72,73,69,69,71,76,71]
# chiều cao trung bình 
a = sum(height_inch)/len(height_inch)
# chiều cao nhất
b = max(height_inch)
c = min(height_inch)
# in ra 3 chiều cao đầu cuối
d  = height_inch[:3]
e = height_inch[-3:]
# sắp xếp tăng dần , nhỏ dần
f = sorted(height_inch)
g = height_inch
h =g.reverse()

# chuyển sang (m)
height_meter = [round(h * 0.0254, 2) for h in height_inch]
