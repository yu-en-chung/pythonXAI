def hello():
    print("hello")


def hello2(name):
    print("hello" + name)


def my_max(a, b):
    if a > b:
        return a
    else:
        return b


def calculate_circle_area(r, pi=3.14, scale=1):
    return (r * scale) ** 2 * pi


hello()
hello2("Tom")
print(my_max(10, 20))
print(calculate_circle_area(10))
print(calculate_circle_area(10, scale=2))
print(calculate_circle_area(10, 3.14159, 2))

print("-" * 20)

length = 5
area = 123


def calculate_square_area():
    # print("面積是", area) #會報錯
    area = length**2
    print("面積是", area)


def calculate_square_area2():
    area = length**2
    return area


def calculate_square_area3():
    global area
    area = length**2


length = 10
calculate_square_area()
print(calculate_square_area2())
calculate_square_area3()
print(area)

print("-" * 20)


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


x1 = float(input("x1:"))
y1 = float(input("y2:"))
x2 = float(input("x2:"))
y2 = float(input("y2:"))
d = distance(x1, y1, x2, y2)
print(f"({x1}, {y1}) 與 ({x2}, {y2}) 的距離為 {d}")
