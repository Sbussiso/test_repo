import streamlit as st
import streamlit_authenticator as stauth

# Authentication
names = ["John Doe", "Jane Doe"]
usernames = ["jdoe", "janedoe"]
passwords = ["abc", "def"]

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
                                     "some_cookie_name", "some_signature_key",
                                     cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    st.write(f"Welcome *{name}*")
    # App code goes here
    
elif authentication_status == False:
    st.error("Username/password is incorrect")
elif authentication_status == None:
    st.warning("Please enter your username and password")
