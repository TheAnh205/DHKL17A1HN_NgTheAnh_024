#xử lí ngoại lệ khi a, b hoặc c không phải kiểu số
try:
    a = eval(input('Nhập đô dài cạnh a: '))
    b = eval(input('Nhập độ dài cạnh b: '))
    c = eval(input('Nhập độ dài cạnh c: '))
except (NameError,ValueError) as er:
    print('Vui lòng nhập kiểu số', er)

#sử lí ngoại lệ khi người dùng nhập giá trị âm hoặc 0 cho a, b hoặc c
def canh_tamgiac():

  sides = []
  count = 0
  while True:
    side = input("Nhập cạnh của tam giác: ")
    try:
      side = int(side)
      if side <= 0:
        count += 1
    except ValueError:
      print("Số nhập không hợp lệ")
      continue

    sides.append(side)

    if len(sides) == 3:
      break

  if count == 1:
    raise ValueError("Số nhập không hợp lệ")

  return sides


if __name__ == "__main__":
  try:
    sides = canh_tamgiac()
    print("Các cạnh của tam giác:", sides)
  except ValueError as e:
    print(e)

#xử lí ngoại lệ khi người dùng nhập a, b hoặc c dương nhưng không thỏa mãn điều kiện tồn tại môt tam giác
def canh_khong_hop_le():


  sides = []
  while True:
    for i in range(3):
      side = input("Nhập cạnh thứ {}: ".format(i + 1))
      try:
        side = int(side)
        if side <= 0:
          raise ValueError("Số nhập không hợp lệ")
      except ValueError:
        print("Số nhập không hợp lệ")
        continue
      sides.append(side)

    if sides[0] + sides[1] <= sides[2] or sides[0] + sides[2] <= sides[1] or sides[1] + sides[2] <= sides[0]:
      raise Exception("Không tồn tại tam giác với các cạnh đã nhập")

    return sides


if __name__ == "__main__":
  try:
    sides = canh_khong_hop_le()
    print("Ba cạnh của tam giác:", sides)
  except Exception as e:
    print(e)