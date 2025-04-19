import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO
import base64

# --- Page Config ---
st.set_page_config(page_title="🔳 QR Code Generator", layout="centered")


st.markdown("""
<style>
/* Style for all buttons */
button[kind="primary"] {
    background-color: #ffaa00 !important;
    color: black !important;
    border: 2px solid #ffaa00 !important;
    border-radius: 6px;
    padding: 8px 16px;
    font-weight: bold;
}

/* Download button also matches the same */
div.stDownloadButton > button {
    background-color: #ffaa00 !important;
    color: black !important;
    border: 2px solid #ffaa00 !important;
    border-radius: 6px;
    font-weight: bold;
    transition: 0.3s ease-in-out;
}

div.stDownloadButton > button:hover {
    background-color: #ffcc33 !important;
    color: black !important;
    border-color: #ffcc33 !important;
}
</style>
""", unsafe_allow_html=True)

st.image("image.png", width=100, use_container_width=True)

# --- Title and Instructions ---
st.title("🔳 QR Code Generator")
st.markdown("Convert your text, URL, or message into a QR Code instantly!")

# --- Input Area ---
user_input = st.text_input("Enter text or URL to encode", placeholder="https://your-link.com")

# --- Generate QR Code ---
if st.button("✨ Generate QR Code"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text or a URL.")
    else:
        # Create QR Code
        qr = qrcode.QRCode(version=1, box_size=10, border=2)
        qr.add_data(user_input)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert("RGB") 

        # --- Display QR code image ---
        st.image(img, caption="📸 Your QR Code", use_container_width=False)

        # --- Download QR as PNG ---
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_bytes = buffered.getvalue()
        b64_img = base64.b64encode(img_bytes).decode()
        href = f'<a href="data:image/png;base64,{b64_img}" download="qr_code.png">📥 Download QR Code</a>'
        st.markdown(href, unsafe_allow_html=True)



# --- Sidebar ---
# st.sidebar.image("https://cdn-icons-png.flaticon.com/512/10480/10480079.png")
st.sidebar.image("qr2.png", width=100, use_container_width=True)

st.sidebar.title("ℹ️ How to Use")
st.sidebar.markdown("""
1. Enter **any text, link, or message** in the input box.  
2. Click on **Generate QR Code**.  
3. Scan or **download** your QR code as an image.  
""")

st.sidebar.markdown("---")

st.sidebar.info("💡 Tip: You can use this to share websites, contact info, Wi-Fi credentials, or just for fun!")

st.sidebar.markdown("---")

# 📬 Contact Section
st.sidebar.markdown("### 📬 Contact")
st.sidebar.write("📧 [Email Us](mailto:ismailahmedshahpk@gmail.com)")
st.sidebar.write("🔗 [Connect on LinkedIn](https://www.linkedin.com/in/ismail-ahmed-shah-2455b01ba/)")
st.sidebar.write("💬 [Chat on WhatsApp](https://wa.me/923322241405)")

st.sidebar.markdown("---")
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135716.png", width=90, use_container_width=True)
st.sidebar.markdown("---")
st.sidebar.markdown("<p style='text-align: center; color: grey;'>Built with ❤️ by Ismail Ahmed Shah</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")
