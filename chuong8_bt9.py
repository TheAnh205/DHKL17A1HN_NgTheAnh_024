import time

def countdown(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1

    print("Countdown finished!")

# Gọi hàm countdown và truyền số giây cần đếm ngược
countdown(10)