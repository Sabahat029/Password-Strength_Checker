import re
import streamlit as st

#page styling
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒", layout="centered")

#custom css
st.markdown(""""
<style>
    .main{text_align: center;}
    .stTextInput {width: 60% !important; margin: auto;} 
    .stButton button {width: 50%; background-color: blue; color: white; font-size: 18px;}                 
    .stButton button:hover {background-color: red; color: white;}
</style>            
""",unsafe_allow_html=True)

#page title & description
st.title("Password Strength Generator")
st.write("Enter your password to check its security level")

#function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >=8:
        score += 1    #increased score by one
    else:
        feedback.append("Password should be atleast 8 characters long.")

    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score =+ 1
    else:
        feedback.append("Password should contain both upper case(i.e.A-Z) and lower case(i.e.a-z)letters.")

    if re.search(r"\d",password):
        score =+ 1
    else:
        feedback.append("Password should contain atleast one number(i.e.0-9).")

    #special characters
    if re.search(r"[!@#$%^&*]",password):
        score =+ 1
    else:
        feedback.append("Password should contain at least one special character(i.e.!@#$%^&*).")

    #display password strength
    if score == 4:
      st.success("Strong password - Your password is secure.")
    elif score == 3:
        st.info("Moderate password - Consider improving by adding more features.")
    else:
        st.error("Weak password - Try improving by following the suggestions below.")

#feedback
    if feedback:
        with st.expander("Improve Your Password"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:",type= "password",help="Make sure your password is strong." )

#button working
if st.button("Check strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please enter a password first.")
