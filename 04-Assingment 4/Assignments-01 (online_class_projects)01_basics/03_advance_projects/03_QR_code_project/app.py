import streamlit as st
import qrcode
import cv2
import numpy as np
from PIL import Image
import io

st.set_page_config(page_title="QR Code Generator", layout="wide")

st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 28px;
            color: gray;
            font-weight: bold;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">QR Code Generator & Decoder</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

def generate_qr_code(data):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white")
    img_bytes = io.BytesIO()
    qr_img.save(img_bytes, format="PNG")
    img_bytes.seek(0)
    return img_bytes

def decode_qr_code(image):
    image_np = np.array(image.convert("RGB"))
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(image_np)
    return data if data else "No QR code detected."


with col1:
    st.subheader("Generate QR Code")
    text = st.text_input("Enter text or URL:")
    if st.button("Generate QR"):
        if text:
            qr_image = generate_qr_code(text)
            st.image(qr_image, caption="Generated QR Code")
            st.download_button("Download QR", qr_image, "qr_code.png", "image/png")
        else:
            st.warning("Please enter some text.")

with col2:
    st.subheader("Decode QR Code")
    uploaded_file = st.file_uploader("Upload a QR Code", type=["png","jpg","jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded QR Code")
        st.write("Decoded Data:", decode_qr_code(image))