import streamlit as st
from compare_images import compare_images
from detect_objects import detect_with_haar
import cv2
import os
from PIL import Image
import io

st.set_page_config(layout="wide")
st.title("🛡️ Exam Proctoring - Image Similarity & Face Detection")

img1 = st.file_uploader("📤 Upload Reference Image", type=["jpg", "jpeg", "png"])
img2 = st.file_uploader("📤 Upload Live Image", type=["jpg", "jpeg", "png"])

if img1 and img2:
    with open("temp1.jpg", "wb") as f:
        f.write(img1.read())
    with open("temp2.jpg", "wb") as f:
        f.write(img2.read())

    # Step 1: Image Similarity
    score, error, diff = compare_images("temp1.jpg", "temp2.jpg")
    st.markdown("### 🧠 Image Similarity Metrics")
    st.success(f"**SSIM Score:** {score:.4f}")
    st.info(f"**Mean Squared Error (MSE):** {error:.2f}")

    # Step 2: Face Detection using Haar
    ref_annotated = detect_with_haar("temp1.jpg", save_as="detected1.jpg")
    live_annotated = detect_with_haar("temp2.jpg", save_as="detected2.jpg")

    # Step 3: Show Side-by-side Images
    st.markdown("### 🖼️ Side-by-Side Image Comparison")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("temp1.jpg", caption="Reference Image", use_column_width=True)
        st.download_button("Download Reference", data=img1, file_name="reference.jpg")

    with col2:
        st.image("temp2.jpg", caption="Live Image", use_column_width=True)
        st.download_button("Download Live", data=img2, file_name="live.jpg")

    with col3:
        st.image(diff, caption="Difference Image", use_column_width=True)
        # Convert diff to bytes
        diff_bytes = io.BytesIO()
        Image.fromarray(diff).save(diff_bytes, format='PNG')
        st.download_button("Download Difference", data=diff_bytes.getvalue(), file_name="diff.png")

    # Step 4: Show Detection Results
    st.markdown("### 🔍 Face Detection Results")
    col4, col5 = st.columns(2)

    with col4:
        st.image("detected1.jpg", caption="Detected Faces in Reference", use_column_width=True)
        with open("detected1.jpg", "rb") as f:
            st.download_button("Download Detected Ref", data=f, file_name="detected_ref.jpg")

    with col5:
        st.image("detected2.jpg", caption="Detected Faces in Live", use_column_width=True)
        with open("detected2.jpg", "rb") as f:
            st.download_button("Download Detected Live", data=f, file_name="detected_live.jpg")

    # Clean up (optional): os.remove("temp1.jpg") etc.
