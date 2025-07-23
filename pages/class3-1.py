print(len([]))
print(len(["蘋果"]))
print(len(["a", "b"]))
print(len([1, 2, 3]))

print("-" * 20)

l = [1, 2, 3]
for i in range(len(l)):
    print(l[i])

print("-" * 20)

for element in l:
    print(element)

print("-" * 20)

l[0] = "A"
l[2] = "c"
print(l)

print("-" * 20)

a = [10, 20, 30]
b = a
b[1] = 200
print(a)  # a 也會變成 [10, 20, 200]

print("-" * 20)

c = [40, 50, 60]
d = c[:]
d[1] = 500
print(c)  # c 不會變成 [40, 500, 60]，因為 d 是 c 的複製品

print("-" * 20)

l1 = [1, 2, 3]
l1.append(4)  # 在串列的最後面加一個元素
print(l1)  # [1, 2, 3, 4]

print("-" * 20)

l2 = ["a", "b", "c", "b", "a"]
l2.remove("b")  # 移除第一個出現的 "b"
print(l2)  # ["a", "c", "b", "a"]

print("-" * 20)

l3 = [1, 2, 3]
l3.pop()  # 移除最後一個元素
print(l3)  # [1, 2]

print("-" * 20)

l4 = [1, 2, 3]
l4.pop(1)  # 移除索引為 1 的元素
print(l4)  # [1, 3]

print("-" * 20)

l5 = [3, 1, 5, 3.3, 4, 2]
l5.sort()  # 將串列排序
print(l5)  # ["1", "2", "3", "4", "5"]

l6 = ["banana", "cherry", "apple"]
l6.sort()  # 將字串串列排序
print(l6)  # ["apple", "banana", "cherry"]
