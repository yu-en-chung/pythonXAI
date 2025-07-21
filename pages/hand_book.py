import streamlit as st

st.write(
    """
這是一份適合國小學生閱讀的 Python 筆記整理，內容簡單易懂，幫助你回顧今天上課學到的東西：

---

# 🐍 Python 入門筆記 - 第 1 課

## 📝 註解是什麼？

### ➤ 註解是寫給「人」看的，電腦不會執行

* **單行註解**：用 `#` 開頭

  ```python
  # 這是單行註解
  ```
* **多行註解**：用三個雙引號 `\"""` 包起來

  ```python
  \"""
  這是
  多行
  註解
  \"""
  ```

---

## 🖨️ 用 `print()` 印出東西

### ➤ 這可以把東西顯示在畫面上：

```python
print(100)  # 印出數字
print(3.14)  # 印出小數
print(True)  # 印出布林值：真
print(False)  # 印出布林值：假
print("Hello World!")  # 印出文字
```

---

## 📦 變數是什麼？

### ➤ 變數就像是「裝東西的小盒子」

```python
a = 10
print(a)  # 印出10

a = 20
print(a)  # 盒子裡的東西變了

a = "apple"
print(a)  # 現在變數裡裝的是文字
```

---

## ➕ 數學運算

| 符號   | 意思     | 範例       |
| ---- | ------ | -------- |
| `+`  | 加法     | `7 + 3`  |
| `-`  | 減法     | `7 - 3`  |
| `*`  | 乘法     | `7 * 3`  |
| `/`  | 除法     | `7 / 3`  |
| `//` | 整數除法   | `7 // 3` |
| `%`  | 餘數（取餘） | `7 % 3`  |
| `**` | 次方     | `2 ** 3` |

---

## 🔤 字串的操作

```python
s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2  # 合併文字，中間加空格
print(s3)  # Hello World

print(s1 + s2 * 3)  # World 重複3次
```

---

## 👶 f-string：把變數放進句子裡

```python
name = "Python"
age = 31
new_str = f"我是{name}，今年{age}歲"
print(new_str)
```

---

## 🔢 了解資料的類型

用 `type()` 來看一個東西是什麼型態：

```python
print(type(True))  # 布林值
print(type(123))  # 整數
print(type(123.0))  # 小數
print(type("hello"))  # 字串
```

---

## 🔁 型態轉換

把一種型態變成另一種：

```python
int("123") → 整數  
float("123") → 小數  
str(1000) → 文字  
bool("") → False（空的東西是假的）  
```

---

## 🎤 使用者輸入

```python
get = input("請輸入一些內容: ")
print(get)
print(type(get))  # 會是字串型態
```

---

## 🧮 小練習：計算圓的面積

```python
r = int(input("請輸入圓的半徑: "))
area = 3.14 * r**2
print(f"圓的面積為: {area}")
```

---

## 🌐 Streamlit：做網頁小工具

```python
import streamlit as st

st.title("這是標題")
st.write("這是write寫的內容")
st.text("這是text寫的內容")
```

### 📄 markdown 可以排版文字：

```markdown
* **粗體文字**
* *斜體文字*
* [連結](https://www.example.com)
* 程式碼區塊：
```python
print("Hello World!")
````
# 這是標題1
## 這是標題2
### 這是標題3
#### 這是標題4

"""
)
