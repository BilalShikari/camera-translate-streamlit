# Real-Time Camera Translation App

A **Streamlit app** that uses your webcam to capture text from images, performs **OCR (Optical Character Recognition)** with Tesseract, and translates it to a target language using **Google Translator**.  

---

## Features

- Real-time webcam input  
- OCR for multiple languages (`eng`, `hin`, `fra`, `deu`, `spa`, `ara`)  
- Translation to any ISO language code (e.g., `en`, `fr`, `hi`, `es`)  
- Streamlit interface for easy interaction  

---

## 1️⃣ Prerequisites

- Python 3.7 or higher  
- Webcam  

---

## 2️⃣ Install Tesseract OCR

### Windows

1. Download the installer: [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)  
2. Install and remember the path (default: `C:\Program Files\Tesseract-OCR\tesseract.exe`)  

### macOS

```bash
brew install tesseract
Linux
bash
Copy
Edit
sudo apt-get install tesseract-ocr
3️⃣ Install Python dependencies
Create and activate a virtual environment:

bash
Copy
Edit
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
Install required packages:

bash
Copy
Edit
pip install streamlit opencv-python pytesseract pillow deep-translator numpy
4️⃣ Running the app locally
Open terminal in your project folder:

bash
Copy
Edit
cd path/to/your/project
Run Streamlit:

bash
Copy
Edit
streamlit run camera_translate.py
Allow camera access.

Select OCR language, enter target translation language code, and point the camera at text.

5️⃣ Push to GitHub
Initialize Git:

bash
Copy
Edit
git init
Add files:

bash
Copy
Edit
git add camera_translate.py requirements.txt README.md
Commit:

bash
Copy
Edit
git commit -m "Initial commit: Streamlit real-time camera translation app"
Link to GitHub repo:

bash
Copy
Edit
git remote add origin https://github.com/<your-username>/camera-translate-streamlit.git
Rename branch to main:

bash
Copy
Edit
git branch -M main
Push:

bash
Copy
Edit
git push -u origin main --force
⚠️ --force is safe if your remote repo is empty or only has a README.

6️⃣ Deploy on Streamlit Cloud
Go to Streamlit Community Cloud

Sign in with GitHub

Click New app → Select repo → main branch → camera_translate.py

Click Deploy

Your app will have a public URL

7️⃣ Notes
Clear printed text works best for OCR.

Use ISO language codes for translation: en (English), fr (French), hi (Hindi), es (Spanish), etc.

Streaming version may use more CPU; reduce frame size or update interval if needed.

pgsql
Copy
Edit

---

This is fully **text-only and ready to paste** into your GitHub README.  

If you want, I can also create a **ready-to-paste `requirements.txt` and a one-command Git push block** to make your repo live immediately.  

Do you want me to do that?
