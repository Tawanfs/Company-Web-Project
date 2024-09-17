import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("The Best Company")
st.text("desc")
st.header("Our Team")

col1, col2, col3 = st.columns(3)

df = pd.read_csv('data (1).csv', sep=',')

with col1:
    for i, row in df[:4].iterrows():
        name = (row['first name'] +' ' + row['last name'])
        st.subheader(name.title())
        st.image('images (3)/' + row['image'])
        st.text(row['role'])     
        
with col2:
    for i, row in df[4:8].iterrows():
        name = (row['first name'] +' ' + row['last name'])
        st.subheader(name.title())
        st.image('images (3)/' + row['image'])
        st.text(row['role'])  
        
with col3:
    for i, row in df[8:].iterrows():
        name = (row['first name'] +' ' + row['last name'])
        st.subheader(name.title())
        st.image('images (3)/' + row['image'])
        st.text(row['role'])  
    
    
