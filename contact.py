import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    
    raw_message = st.text_area("Your Message")
    
    message =f"""\
        Subject: Mail from webapp
        \
        From:{user_email}
        {raw_message}
    """
    
    button = st.form_submit_button("submit")
    
    if button:
        print("Submitted")
        send_email(message)
        st.info("Your Email is Send Successfully!")