import streamlit as st
import re
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, red, blue);
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Compile the password pattern
pattern = re.compile(
    r'(?=.*[A-Z])'        # At least one uppercase letter
    r'(?=.*[a-z])'        # At least one lowercase letter
    r'(?=.*\d)'           # At least one digit
    r'(?=.*[!@#$%^&*])'   # At least one special character
    r'[A-Za-z\d!@#$%^&*]{8,}'  # Minimum 8 characters
)

# Streamlit UI
st.title("Password Validator")

password = st.text_input("Enter your password", type="password")

if st.button("Check Password"):
    if pattern.fullmatch(password):
        st.success("Password is valid.")
    else:
        st.error("Invalid password.")
        st.write("Your password must:")
        st.write("- Be at least 8 characters long")
        st.write("- Contain at least one uppercase letter")
        st.write("- Contain at least one lowercase letter")
        st.write("- Contain at least one digit")
        st.write("- Contain at least one special character (!@#$%^&*)")