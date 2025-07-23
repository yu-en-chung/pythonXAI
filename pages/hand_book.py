import streamlit as st
import os

fire_path = "markdown"
fires = os.listdir(fire_path)
fires.sort()
for fire in fires:
    if fire.endswith(".md"):
        with open(f"{fire_path}/{fire}", "r", encoding="utf-8") as f:
            content = f.read()
        with st.expander(fire[:-3] + "課堂筆記"):
            st.write(content)
