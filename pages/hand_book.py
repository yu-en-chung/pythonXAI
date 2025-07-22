import streamlit as st

with st.expander("class 1 課堂筆記"):
    st.write(
        """

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

with st.expander("class 2 課堂筆記"):
    st.write(
        """
---
# 🐍 Python 第二堂課筆記（簡單易懂版）
---

## 🔍 比較運算子（比一比）

這些符號可以拿來比數字：

```python
print(1 == 2)   # 等不等於 → False
print(1 != 2)   # 不等於 → True
print(1 >= 2)   # 大於或等於 → False
print(1 <= 2)   # 小於或等於 → True
print(1 > 2)    # 大於 → False
print(1 < 2)    # 小於 → True
```

---

## 🧠 邏輯運算子（用來判斷的魔法字）

```python
print(not True)      # 不是 → False
print(not False)     # 不是 → True

print(True and True)     # 而且都要對 → 才會 True
print(True and False)    # 一個錯就 False

print(True or False)     # 有一個對就 True
print(False or False)    # 兩個都錯才 False
```

---

## 🔐 密碼小遊戲（`if` 判斷）

### 判斷密碼對不對

```python
password = input("請輸入密碼: ")

if password == "1234":
    print("密碼正確")
else:
    print("密碼錯誤")
```

### 多個密碼選擇

```python
if password == "1234":
    print("歡迎 Ray")
elif password == "5678":
    print("歡迎 Mike")
else:
    print("密碼錯誤")
```

---

## 🗓️ 判斷是不是閏年

### 方法一（巢狀 if）

```python
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("是閏年")
        else:
            print("不是閏年")
    else:
        print("是閏年")
else:
    print("不是閏年")
```

### 方法二（比較簡單）

```python
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("是閏年")
else:
    print("不是閏年")
```

---

## 📊 使用 Streamlit 做小互動（像網頁一樣的程式）

### 顯示你輸入的數字

```python
import streamlit as st

number = st.number_input("請輸入一個數字", step=1, min_value=0, max_value=100)
st.write(f"你輸入的數字是: {number}")
```

### 成績評分系統

```python
score = st.number_input("請輸入分數", step=1, min_value=0, max_value=100)

if score >= 90:
    st.write("你的等第是 A")
elif score >= 80:
    st.write("你的等第是 B")
elif score >= 70:
    st.write("你的等第是 C")
elif score >= 60:
    st.write("你的等第是 D")
else:
    st.write("你的等第是 E")
```

### 按鈕特效

```python
if st.button("點我"):
    st.balloons()  # 放氣球 🎈

if st.button("點我一下"):
    st.snow()  # 下雪 ❄️
```

---

## 🔁 for 迴圈（重複做事情）

```python
for i in range(10):     # 從 0 到 9
    print(i)

for i in range(2, 6):   # 從 2 到 5
    print(i)

for i in range(2, 10, 2):  # 從 2 開始每次加 2（2, 4, 6, 8）
    print(i)
```

---

## ⛰️ 金字塔練習（變出圖形）

### 數字金字塔

```python
num1 = 3
# 輸出：
# 1
# 22
# 333
```

### 箭頭金字塔

```python
num2 = 3
# 輸出：
#   *
#  ***
# *****
#   *
#   *
#   *
```

---

## 📋 串列 List（很多東西放在一起）

```python
L1 = []                          # 空的
L2 = ["蘋果"]
L3 = ["蘋果", "香蕉", "橘子"]
L4 = [1, 2, 3, 4, 5]
L5 = [1, "蘋果", True, 3.14]
L6 = [1, 2, 3, ["蘋果", "香蕉"]]  # 裡面還有一個串列
```

### 怎麼拿出裡面的東西？

```python
print(L6[1])         # 印出第2個：2
print(L6[3][0])      # 印出第4個裡面的第1個 → 蘋果
```

### 串列切片技巧

```python
L = [1, 2, 3, "a", "b", "c"]
print(L[1:4:2])  # 從第2個開始到第4個，每隔一個取 → [2, "a"]
print(L[1:4])    # 第2到第4個 → [2, 3, "a"]
print(L[::2])    # 每隔一個取 → [1, 3, "b"]
```

---

"""
    )
