n = int(input("Nhập số lượng số lẻ : "))

sequence = [i for i in range(1, 2 * n, 2)]

reversed_sequence = list(reversed(sequence))

print("Dãy số lẻ sau khi đảo ngược:", reversed_sequence)