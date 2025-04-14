import streamlit as st
import re
import random
import string

# --- Constants ---
WEAK_PASSWORDS = {"password123", "123456", "qwerty", "welcome", "admin", "passw0rd", "123456789"}

# --- Helper Functions ---
def check_password_strength(password):
    score = 0
    suggestions = []

    if password.lower() in WEAK_PASSWORDS:
        return 0, ["⚠️ This password is commonly used and unsafe. Try something unique!"]

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append(" Use at least 8 characters.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append(" Mix UPPER and lower case letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append(" Include numbers (0-9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append(" Add special characters (!@#$...).")

    return score, suggestions

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+"
    return ''.join(random.choice(characters) for _ in range(length))

# --- Streamlit Page Config ---
st.set_page_config(page_title="SecurePass Vault", page_icon="🛡️", layout="centered")

# --- Custom Heading ---
st.markdown("""
    <h1 style='text-align: center; background:linear-gradient(to right, #4e3629, #9e7e44);
    -webkit-background-clip: text; color: transparent; font-size: 3em;'> SecurePass Vault</h1>
    <div style="text-align: center; font-size: 18px; color: #555;">
        Empower your online safety — check your password strength or generate a hacker-proof one instantly!
    </div>
    <br>
""", unsafe_allow_html=True)

# --- Main App ---
option = st.radio("✨ Choose an Option:", [" Check Password Strength", " Generate Strong Password"])

if option == " Check Password Strength":
    password = st.text_input("Enter your password", type="password", placeholder="Type here securely...")
    if st.button("Check Now"):
        if password:
            score, feedback = check_password_strength(password)
            if score == 4:
                st.success(" Excellent! This password is super strong!")
            elif score == 3:
                st.warning(" Almost there! A few tweaks could make it perfect.")
            else:
                st.error(" Weak password. Follow the suggestions to improve.")

            st.markdown("###  Suggestions:")
            for tip in feedback:
                st.write("- " + tip)
        else:
            st.info(" Please enter a password to analyze.")

elif option == " Generate Strong Password":
    length = st.slider("Select Desired Password Length", 8, 24, 12)
    if st.button("Generate Secure Password"):
        strong_password = generate_password(length)
        st.success("🎉 Your Secure Password:")
        st.code(strong_password, language="")

# --- Footer ---
st.markdown("""
    <br><hr>
    <div style="text-align: center; font-size: 14px; color: gray;">
         Built with love by <b>Urooj Saeed</b> | Stay secure, stay smart 
    </div>
""", unsafe_allow_html=True)
