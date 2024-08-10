import streamlit as st
from send_email import send_email
st.header("Contact me")

with st.form(key= "email_form"):
    user_email = st.text_input("your email address")
    subject=st.text_input("subject")

    #message= st.text_area("your message")
    #message = + "\n"+ user_email
    
    raw_message=st.text_area("your message")
    
    message =f"""\
    from:{user_email}
    {raw_message}
    """
    button =st.form_submit_button()

    if button:
        print("submitted")
        print(button)
        send_email(subject,message)
        st.info("your email is send successful !")