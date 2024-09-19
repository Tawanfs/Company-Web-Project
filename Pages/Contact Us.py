import streamlit as st
import funcs as funcs


with st.form(key='email_form'):
    user_email = st.text_input("Email", key="email")
    user_choice = st.selectbox("Topic", options=("", "Job Inquiries", "Project Proposals", "Other"), key="topic") 
    user_message = st.text_area("Describe", key="text")
    user_submited = st.form_submit_button("Submit")
    if user_submited:
        funcs.send_mail(message=f"{user_choice}\n {user_message}\n {user_email}")
        st.info("The Email Was Sent Successfully")


