import streamlit as st
import pandas as pd
st.title("การทดสอบสร้างเว็บด้วยPython")
st.image("./image/bens.jpeg")
st.header("การนำเสนอข้อมูลกราฟด้วย Python") 

col1, col2, col3 = st.columns(3)

with col1:
    st.header("versincolor")
    st.image("./image/versicolor.jpg")

with col2:
    st.header("verginica")
    st.image("./image/virginica.jpg")

with col3:
    st.header("setosa")
    st.image("./image/setosa.jpg")

    #import pandas ad pd
df=pd.read_csv("./data/iris.csv")


if(st.button("แสดงข้อมูลตัวอย่าง")):
    st.write(df.head(10))
    st.button("ไม่แสดงข้อมูลตัวอย่าง")

else:
    st.button("ไม่แสดงข้อมูลตัวอย่าง")

