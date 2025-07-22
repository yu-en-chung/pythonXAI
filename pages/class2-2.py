import streamlit as st

number = st.number_input("請輸入一個數字", step=1, min_value=0, max_value=100)

st.write(f"你輸入的數字是: {number}")

st.write("## 練習")
score = st.number_input("請輸入分數", step=1, min_value=0, max_value=100)
if score >= 90:
    st.write("你的等第是A")
elif score >= 80 and score < 90:  # and後面可省略
    st.write("你的等第是B")
elif score >= 70 and score < 80:  # and後面可省略
    st.write("你的等第是C")
elif score >= 60 and score < 70:  # and後面可省略
    st.write("你的等第是D")
else:
    st.write("你的等第是E")

st.button("點我", key="button1")

if st.button("點我", key="button2"):
    st.balloons()

if st.button("點我", key="button3"):
    st.snow()
