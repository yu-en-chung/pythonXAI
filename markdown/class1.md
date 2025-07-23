---
# 🐍 Python 第ㄧ堂課筆記（簡單易懂版）
---

## 🧠 什麼是 Python？

Python 是一種很厲害又簡單的程式語言，我們可以用它來畫圖、算數學、玩遊戲，還可以讓電腦聽我們的話！

---

## ✏️ 註解是什麼？

寫程式時可以加上「註解」，讓自己或別人知道這段程式碼在做什麼。

```python
# 這是單行註解（用一個 # 開頭）

"""
這是
多行
註解（用三個雙引號包起來）
"""
```

---

## 📤 用 print 把東西顯示出來

```python
print(100)  # 顯示數字
print(3.14)  # 顯示小數
print(True)  # 顯示布林值（對或錯）
print("Hello")  # 顯示文字
```

---

## 📦 變數：幫資料取名字

```python
a = 10
print(a)  # 顯示 a 的值（現在是 10）

a = "apple"
print(a)  # a 現在變成 "apple"
```

---

## ➕ 加減乘除也會！

```python
print(7 + 3)  # 加法：10
print(7 - 3)  # 減法：4
print(7 * 3)  # 乘法：21
print(7 / 3)  # 除法（會有小數）
print(7 // 3)  # 整數除法（只留下整數）
print(7 % 3)  # 餘數：1
print(2**3)  # 次方：2 的 3 次方 = 8
```

---

## 🔤 字串（文字）的玩法

```python
s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2
print(s3)  # Hello World

print(s1 + s2 * 3)  # HelloWorldWorldWorld
```

---

## 🧮 f-string：快速放入變數

```python
name = "Python"
age = 31
print(f"我是{name}，今年{age}歲")
```

---

## 📏 算長度、看類型

```python
print(len("Hello"))  # 字串長度
print(type(123))  # 看這個是什麼類型（整數 int）
```

---

## 🧙‍♂️ 型別轉換魔法

```python
int("123")  # 把字串變成數字
float("123")  # 變成小數
str(1000)  # 變成字串
bool(0)  # False
bool("hello")  # True
```

---

## 🎤 讓使用者輸入東西

```python
get = input("請輸入一些內容: ")
print(get)
```

---

## 🧮 小挑戰：計算圓面積

```python
r = int(input("請輸入圓的半徑: "))
area = 3.14 * r ** 2
print(f"圓的面積為: {area}")
```

---

## 🌐 Streamlit：把程式變成網頁！

先在程式開頭加這行：

```python
import streamlit as st
```

然後就可以做出漂亮的網頁畫面：

```python
st.title("這是標題")
st.write("這是 write 寫的內容")
st.text("這是 text 寫的內容")
```

還可以用 Markdown 讓內容變得更酷：

````python
st.markdown("""
* **粗體文字**
* *斜體文字*
* [連結](https://www.example.com)
* 程式碼範例:
```python
print("Hello World!")
````

# 大標題

## 中標題

### 小標題

""")

```

---

## ✅ 小提醒
- `input()` 得到的都是字串，要記得用 `int()` 或 `float()` 轉換。
- `print()` 可以一次印出很多東西，用逗號分開就行。
- `type()` 幫我們看變數的類型。

---

如果你每天練習一點點，Python 就會變成你最好的超能力工具 💪🐍
加油，未來的程式高手！

---
需要我幫你做成 PDF 小冊子或加入插圖的話，也可以再告訴我喔！
```
