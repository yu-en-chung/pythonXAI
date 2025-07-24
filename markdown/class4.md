---
# 🐍 Python 第四堂課筆記（簡單易懂版）
---

## 💡 第 1 部分：字典（Dictionary）

字典就像一本小小的字典書，可以幫你找到「關鍵字」對應的「內容」。

```python
d = {"apple": "蘋果", "banana": "香蕉"}
print(d["apple"])  # 印出 蘋果
```

### 📚 常用方法：

```python
# 走訪所有 key（關鍵字）
for key in d.keys():
    print(key)

# 走訪所有 value（對應的值）
for value in d.values():
    print(value)

# 同時走訪 key 和 value
for key, value in d.items():
    print(f"{key}: {value}")
```

### ✏️ 更改與刪除：

```python
d[2] = "二"  # 更改或新增
v = d.pop(1)  # 刪除 key 為 1 的資料
print(f"刪除的值: {v}")
```

### 🔍 查找是否存在：

```python
print(2 in d)  # 看看 2 是不是在字典裡
```

## 🌄 額外練習：水果在不在？

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # True
print("orange" in fruits)  # False
```

---

## 🖼️ 第 2、3 部分：做一個圖片購物平台（使用 Streamlit）

我們用 Streamlit 做了一個簡單的購物網站：

### ✅ 有哪些功能？

1. 顯示圖片、商品名稱、價格、庫存
2. 可以購買商品（庫存會減少）
3. 可以補充庫存
4. 自訂每排幾個欄位（商品數）

```python
import streamlit as st
# 顯示圖片與商品資訊
st.image("image/apple.jpg")
st.write("價格: $10")
st.write("庫存: 10")
```

🎯 我們還會用 `session_state` 來記住商品資料（這樣重新整理也不會不見！）

---

## 🔁 第 4 部分：自訂的函式（function）

函式就像是小機器，你可以給它一些「輸入」，它會幫你算出「結果」。

```python
def hello():
    print("hello")

def hello2(name):
    print("hello " + name)

def my_max(a, b):
    return a if a > b else b
```

### 🔢 函式可以幫我們算圓面積：

```python
def calculate_circle_area(r, pi=3.14, scale=1):
    return (r * scale) ** 2 * pi
```

### ⚠️ 注意：函式裡的變數作用範圍（全域與區域）

```python
def calculate_square_area():
    area = length ** 2  # 這裡的 area 跟外面不一樣！
```

---

## 📏 額外應用：算距離！

輸入兩個點的位置，幫你算它們的距離：

```python
def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
```

---

## 🎲 第 5 部分：骰子遊戲

我們讓電腦幫我們擲骰子很多次，看看每個數字出現幾次！

```python
import random

def roll_dice(n):
    result = []
    for i in range(n):
        number = random.randint(1, 6)
        result.append(number)
    return result
```

### ✏️ 統計出現次數：

```python
count = [0, 0, 0, 0, 0, 0]
for num in outcome:
    count[num - 1] += 1
```

---

## 🎉 總結

| 學到什麼？      | 說明                                   |
| --------------- | -------------------------------------- |
| `dict` 字典     | 用來對應資料（像是「英文：中文」）     |
| `for` 迴圈      | 可以一次處理很多資料                   |
| `in`            | 可以檢查某樣東西有沒有在裡面           |
| `function` 函式 | 幫你重複做事情                         |
| `Streamlit`     | 做簡單的網站和視覺化介面               |
| `random`        | 讓電腦幫我們做隨機的事情（像是擲骰子） |

---
