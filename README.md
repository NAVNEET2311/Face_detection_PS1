# 🧠 Image Analysis & Face Detection Web App

This project is a Python-based Streamlit web application that allows users to **compare two images** using SSIM and MSE, and **detect faces** using Haar Cascades. It is particularly useful for verifying the identity of candidates across webcam sessions in online assessments.

---

## 📸 Features

- ✅ **Image Comparison**
  - **SSIM (Structural Similarity Index):** Measures perceptual similarity between two images.
  - **MSE (Mean Squared Error):** Measures average squared pixel difference between two images.

- 🧍‍♂️ **Face Detection**
  - Utilizes OpenCV’s Haar Cascades to detect human faces in uploaded images.
  - Annotates and saves output images with bounding boxes.

- 🌐 **Streamlit Web Interface**
  - Upload two images through a clean, simple UI.
  - View face detection output and similarity comparison results.

---

## 📁 Project Structure

```plaintext
scripts/
├── app.py                 # Optional orchestration script
├── compare_images.py      # Image similarity using SSIM and MSE
├── detect_objects.py      # Face detection using Haar Cascades
├── streamlit_app.py       # Main Streamlit web app
├── detected1.jpg          # Annotated output from image 1
├── detected2.jpg          # Annotated output from image 2
├── temp1.jpg              # Temporary file for uploaded image 1
├── temp2.jpg              # Temporary file for uploaded image 2
├── check-libs.py          # Dependency checker script
└── __pycache__/           # Python cache files
