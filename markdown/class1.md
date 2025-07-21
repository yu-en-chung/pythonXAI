🐍 今天學到的 Python 小筆記
📝 註解是什麼？
註解是給人看的，程式看不懂，不會執行。

分兩種：

單行註解：用 # 開頭
例如：# 這是註解

多行註解：用 """ 把好幾行包起來
例如：

python
複製
編輯
"""
這是
很多行的
註解
"""
📤 顯示東西出來（print）
用 print() 就可以把東西顯示在畫面上。

python
複製
編輯
print(100) # 整數
print(3.14) # 小數
print(True) # 布林值（是）
print(False) # 布林值（不是）
print("Hello World!") # 字串（就是文字）
📦 變數是什麼？
變數就像是一個小盒子，可以裝東西！

python
複製
編輯
a = 10
print(a) # 顯示 a 裡的東西，就是 10

a = 20
print(a) # 現在變成 20

a = "apple"
print(a) # 現在是字串「apple」
➕ 算數也可以做！
python
複製
編輯
print(7 + 3) # 加法 → 10
print(7 - 3) # 減法 → 4
print(7 _ 3) # 乘法 → 21
print(7 / 3) # 除法（會有小數）→ 2.333...
print(7 // 3) # 整數除法（只看整數）→ 2
print(7 % 3) # 取餘數 → 1
print(2 \*\* 3) # 次方 → 2 的 3 次方=8
🔤 字串可以這樣玩
python
複製
編輯
s1 = "Hello"
s2 = "World"
print(s1 + s2) # 接在一起 → HelloWorld
print(s1 + " " + s2) # 中間加空格 → Hello World
print(s1 + s2 _ 3) # 把 s2 重複 3 次 → HelloWorldWorldWorld
🧮 f-string 超好用！
可以把變數放進句子裡！

python
複製
編輯
name = "Python"
age = 31
print(f"我是{name}，今年{age}歲") # → 我是 Python，今年 31 歲
📏 len() 是用來算字的長度
python
複製
編輯
print(len("")) # 空字串 → 0
print(len("Hello")) # → 5
🧐 type() 是用來看資料類型的
python
複製
編輯
print(type(True)) # 布林值
print(type(123)) # 整數
print(type(123.0)) # 小數
print(type("hello")) # 字串
🔁 互相轉換
python
複製
編輯
print(int("123")) # 字串變整數 → 123
print(float("123")) # 字串變小數 → 123.0
print(str(1000)) # 整數變字串 → "1000"
print(bool(0)) # → False
print(bool("hello")) # → True
⌨️ input() 讓使用者輸入
python
複製
編輯
get = input("請輸入一些內容: ")
print(get)
print(type(get)) # 所有輸入的東西都是字串喔！
🧮 小練習：算圓面積！
python
複製
編輯
r = int(input("請輸入圓的半徑:"))
area = 3.14 \* r\*\*2
print(f"圓的面積為: {area}")
🖥️ 使用 Streamlit 做漂亮的網頁介面！
要先寫：import streamlit as st

常用指令：
python
複製
編輯
st.title("這是標題") # 大大的標題
st.write("這是 write 寫的內容") # 顯示文字
st.text("這是 text 寫的內容") # 顯示純文字
用 markdown 寫出更漂亮的格式：
python
複製
編輯
st.markdown(
"""

- **粗體文字**
- _斜體文字_
- [連結](https://www.example.com)
- 程式碼：

```python
print("Hello World!")
這是標題1
這是標題2
這是標題3
"""
)

yaml
複製
編輯

---

這就是你今天學到的所有 Python 指令囉！記得多練習，寫程式就會越來越厲害 💪🐍

需要我幫你做成圖表或小卡片筆記，也可以再說喔！
```
