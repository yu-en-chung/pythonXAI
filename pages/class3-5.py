import random

target = random.randint(1, 101)

while True:
    guess = int(input("請輸入一個數字"))
    if guess < target:
        print("再大一點")
    elif guess > target:
        print("再小一點")
    else:  # guess == target
        print("猜中了")
        break
