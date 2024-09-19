import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("Tech Innovators Inc.")
st.write("""Tech Innovators Inc. is a leading software development company dedicated to delivering cutting-edge technology solutions. Our team of skilled developers, designers, and engineers work collaboratively to create innovative software products that drive business success.
""")
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
    
    
