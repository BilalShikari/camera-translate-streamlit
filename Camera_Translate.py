import os
import cv2
import numpy as np
from PIL import Image
import pytesseract
import streamlit as st
from deep_translator import GoogleTranslator

# ------------------------
# Handle Tesseract path on Windows
# ------------------------
if os.name == "nt":
    tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    if os.path.exists(tesseract_path):
        pytesseract.pytesseract.tesseract_cmd = tesseract_path

# ------------------------
# OCR + Translation function
# ------------------------
def ocr_translate(image, ocr_lang="eng", target_lang="en"):
    if image is None:
        return "No image received."

    # Convert PIL -> OpenCV BGR
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Preprocessing
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 31, 11
    )

    # OCR
    try:
        extracted = pytesseract.image_to_string(thresh, lang=ocr_lang).strip()
    except Exception as e:
        return f"OCR Error: {e}"

    if not extracted:
        return "No text detected. Try clearer text and good lighting."

    # Translation
    try:
        translation = GoogleTranslator(source='auto', target=target_lang).translate(extracted)
    except Exception:
        translation = "(Translation failed. Check language code or internet connection.)"

    return f"Original ({ocr_lang}):\n{extracted}\n\nTranslated → {target_lang}:\n{translation}"

# ------------------------
# Streamlit UI
# ------------------------
st.title("Real-Time Camera Translation")
st.markdown("Take a picture of printed text with your webcam. Select OCR language and target translation language.")

# Webcam input
img_file_buffer = st.camera_input("Capture text")

# Language options
ocr_lang = st.selectbox(
    "OCR Language (Tesseract code)",
    ["eng", "hin", "ara", "fra", "deu", "spa"],
    index=0
)

target_lang = st.text_input(
    "Translate to (ISO code, e.g., en, fr, hi, es, ar, de, spa)",
    value="en"
)

# Process button
if st.button("Translate") and img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    result = ocr_translate(image, ocr_lang, target_lang)
    st.text(result)
