# ADVANCED-IMAGE-STEGANOGRAPHY-USING-LSB-TECHNIQUE
A Python-based desktop application that hides secret text messages inside images using LSB (Least Significant Bit) steganography combined with Fernet encryption for double-layer security. The app features a clean Tkinter GUI and an integrated email sending option to share the stego image securely.
# 📷 Image Steganography Tool with Email Integration  

A **Python-based desktop application** that hides secret text messages inside images using **LSB (Least Significant Bit) steganography** combined with **Fernet encryption** for double-layer security. The app features a clean **Tkinter GUI** and an integrated **email sending** option to share the stego image securely.  

---

## ✨ Features  
- 🔒 **Hide Text in Images** – Embed secret messages in PNG images without noticeable changes.  
- 🔑 **Fernet Encryption** – Encrypt the message before hiding it for added protection.  
- 📧 **Email Integration** – Send the stego image directly to a recipient via Gmail SMTP.  
- 🗝 **Extract Hidden Text** – Retrieve and decrypt messages from stego images using the shared key.  
- 🎨 **User-Friendly Interface** – Modern Tkinter UI with a project info page.  

---

## 🛠 Tech Stack  
- **Python 3**  
- **Tkinter** – GUI  
- **Pillow** – Image processing  
- **cryptography** – Fernet encryption/decryption  
- **smtplib** – Sending emails with attachments  
- **HTML** – Project info documentation  

---


---

## 🚀 Getting Started  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/your-username/image-steganography.git
cd image-steganography
pip install -r requirements.txt
python practice.py

