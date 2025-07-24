import random


def roll_dice(n):
    save = []
    for i in range(n):
        number = random.randint(1, 6)
        save.append(number)
    return save


N = int(input("次數:"))
outcome = roll_dice(N)

print("結果", outcome)

count = [0, 0, 0, 0, 0, 0]
for num in outcome:
    count[num - 1] += 1
for i in range(len(count)):
    print(f"{i+1}出現{count[i]}次")

# n1 = 0
# n2 = 0
# n3 = 0
# n4 = 0
# n5 = 0
# n6 = 0

# for num in outcome:
#     if num == 1:
#         n1 += 1
#     elif num == 2:
#         n2 += 1
#     elif num == 3:
#         n3 += 1
#     elif num == 4:
#         n4 += 1
#     elif num == 5:
#         n5 += 1
#     else:
#         n6 += 1

# print("1出現", n1, "次")
# print("2出現", n2, "次")
# print("3出現", n3, "次")
# print("4出現", n4, "次")
# print("5出現", n5, "次")
# print("6出現", n6, "次")
