import streamlit as st
import funcs as funcs



with st.form(key='email_form'):
    user_email = st.text_input("Email", key="email")
    user_choice = st.selectbox("Topic", options=("", "Job Inquiries", "Project Proposals", "Other"), key="topic") 
    user_message = st.text_area("Describe", key="text")
    user_submited = st.form_submit_button("Submit")
    if user_submited:
        message = f"{user_email}\nTopic: {user_choice}\n{user_message}"
        funcs.send_mail(message)
        st.info("The Email Was Sent Successfully")


