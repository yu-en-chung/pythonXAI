---
# 🐍 Python 第三堂課筆記（簡單易懂版）
---

## 🧮 一、關於串列 (list)

串列就像是一個裝東西的盒子，可以裝很多項目，而且順序不會亂掉！

```python
print(len([1, 2, 3]))
```

➡️ `len()` 是用來數一數「串列裡面有幾個東西」

---

```python
l = [1, 2, 3]
for i in range(len(l)):
    print(l[i])
```

➡️ 這樣可以一個一個把串列裡的東西印出來。

也可以這樣寫，意思一樣：

```python
for element in l:
    print(element)
```

---

### 📦 改變串列裡的東西：

```python
l[0] = "A"
l[2] = "c"
print(l)
```

➡️ 這是在改「第 0 個」和「第 2 個」的內容。

---

### 📋 串列是會連動的！

```python
a = [10, 20, 30]
b = a
b[1] = 200
print(a)
```

➡️ `b = a` 是「一起用同一個盒子」，所以改 b，其實 a 也會變！

如果你想要複製一個新的盒子：

```python
c = [40, 50, 60]
d = c[:]
d[1] = 500
print(c)
```

➡️ `d = c[:]` 是「複製一份新的」，這樣就不會互相影響！

---

## 🛠️ 常用串列功能

```python
l1.append(4)
```

✅ `append()`：加東西到最後面。

```python
l2.remove("b")
```

✅ `remove()`：刪掉第一個出現的東西。

```python
l3.pop()
l4.pop(1)
```

✅ `pop()`：移除最後一個 / 指定位置的東西。

```python
l5.sort()
l6.sort()
```

✅ `sort()`：幫串列裡的東西照順序排好！

---

## 🖼️ 二、做一個介面（用 streamlit）

你可以用 `streamlit` 做出有按鈕、輸入框的畫面！

```python
import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)
col1.button("按鈕1")
col2.button("按鈕2")
```

可以這樣分欄位，有左邊按鈕、右邊按鈕。

---

### ✏️ 輸入框

```python
text = st.text_input("請輸入文字")
st.write("你輸入的文字是:", text)
```

使用者打什麼，就顯示什麼。

---

### 🔄 記住變數：`session_state`

```python
if "var1" not in st.session_state:
    st.session_state.var1 = 1
```

✅ `st.session_state` 可以記住變數的值，不會因為畫面更新就忘記！

---

## 🍔 三、點餐機小專案

用 `streamlit` 做一個點餐系統！

```python
if "order" not in st.session_state:
    st.session_state.order = []
```

✅ 記住你的點餐內容

```python
col1.text_input("請輸入餐點")
col2.button("加入")
```

✅ 可以輸入餐點名稱，再按下按鈕加入購物籃。

```python
col3.write(餐點名稱)
col4.button("刪除")
```

✅ 一樣可以刪掉你不想要的東西！

---

## 🔁 四、迴圈（重複做事情）

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

✅ `while` 是「只要條件成立就一直做」

```python
for i in range(5):
    print(i)
```

✅ `for` 是「做幾次就結束」

```python
if i == 3:
    break
```

✅ `break` 是「提早跳出迴圈」

---

## 🎲 五、亂數（做出隨機數字）

```python
import random

random.randrange(1, 4)  # 會出現 1、2、3
random.randrange(0, 10, 2)  # 出現 0~8 的偶數
random.randint(1, 100)  # 包含 1 和 100 的整數
```

你可以用這些方式讓電腦幫你出「隨機題目」、「抽獎」等等！

---

## ❓ 六、猜數字遊戲

```python
target = random.randint(1, 101)
guess = int(input("請輸入一個數字"))
```

電腦選一個數字，你一直猜，直到猜中為止！

```python
if guess < target:
    print("再大一點")
elif guess > target:
    print("再小一點")
else:
    print("猜中了")
```

---

## 🎁 七、一番賞抽獎機

這是一個「100 張獎券只有 1 張中獎」的小遊戲：

```python
table = [0] * 100
target = random.randint(1, 100)
table[target - 1] = 1
```

每次抽一張：

- 抽到沒中 = 繼續抽
- 抽到中獎 = 結束！
- 抽過了 = 不算、重抽！

最後算出總共抽幾次、花了多少錢：

```python
print(f"總共抽了 {count} 次, 花費 {count * 200} 元")
```

---
