import streamlit as st

with st.form(key='email_form'):
    user_email = st.text_input("Email", key="email")
    user_choice = st.selectbox("Topic", options=("", "Job Inquiries", "Project Proposals", "Other"), key="topic") 
    user_message = st.text_area("Describe", key="text")
    user_submited = st.form_submit_button("Submit")
    if user_submited:
        st.text(user_email)


