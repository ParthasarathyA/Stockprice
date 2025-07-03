import streamlit as st

st.header("_Streamlit_ is :blue[cool] :sunglasses:")

code = '''def hello():
    print("Hello, Parthasarathy!")'''
st.code(code, language="python")
agree = st.checkbox("Are you Awesome?")

if agree:
    st.write("Yes, You're.")