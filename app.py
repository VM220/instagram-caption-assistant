import streamlit as st
from PIL import Image
from utils import generate_caption

st.set_page_config(page_title="AI Instagram Caption Assistant", layout="centered")

st.title("📸 AI Instagram Caption Assistant")

option = st.radio("Choose input type:", ["Upload an image", "Enter a post description"])

if option == "Upload an image":
    uploaded_file = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        description = st.text_input("What's this post about?")
        if st.button("Generate Caption"):
            with st.spinner("Creating your perfect caption..."):
                caption = generate_caption(description)
                st.success("✅ Here's your caption:")
                st.text_area("Generated Caption", caption, height=100)
elif option == "Enter a post description":
    description = st.text_area("Write your post description")
    if st.button("Generate Caption"):
        with st.spinner("Generating..."):
            caption = generate_caption(description)
            st.success("✅ Your Caption:")
            st.text_area("Generated Caption", caption, height=100)
