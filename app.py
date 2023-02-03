import qrcode as qr
import streamlit as st
import validators as v
from PIL import Image

logo = Image.open('./favicon.png')
st.set_page_config(page_title="QR Coder", page_icon=logo)
st.title("QR code Generator")

st.write("")
st.write("")

st.markdown("##### Enter full url like : https://www.google.com")

st.write("")
st.write("")

st.markdown("#### Workes for any url")

st.write("")
st.write("")


def run():
    img = qr.make(url)

    img.save("image.jpg")

    st.image("image.jpg")


url = st.text_input("Enter your URL", "")

valid = v.url(url)


if url != "" and url != " ":
    if valid:
        st.write("")
        st.write("")
        run()
        st.balloons()
    else:
        st.warning("❌ Invalid Entry")
