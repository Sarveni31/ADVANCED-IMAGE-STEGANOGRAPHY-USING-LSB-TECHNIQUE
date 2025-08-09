import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
from cryptography.fernet import Fernet, InvalidToken
import os
import webbrowser
import tempfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

# ---------- Configuration ----------
LOGO_PATH = r"icon.png"
DELIMITER = "1111111111111110"  # sentinel to indicate end of payload

# -------------------- Project Info (HTML) --------------------
def project_info():
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Project Information</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f4f4f4;
                color: #333;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background-color: #fff;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                position: relative;
            }
            .logo {
                position: absolute;
                top: 20px;
                right: 20px;
            }
            .logo img {
                height: 80px;
                width: auto;
            }
            h1 {
                color: #d9534f;
                text-align: center;
                margin-bottom: 20px;
            }
            p {
                line-height: 1.6;
                margin-bottom: 10px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 10px;
                text-align: left;
            }
            th {
                background-color: #d9534f;
                color: white;
            }
            a {
                color: #d9534f;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
            .footer {
                text-align: center;
                margin-top: 30px;
                font-size: 0.9em;
                color: #777;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="logo">
               <img src="data:image/jpeg;base64,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" alt="Company Logo" style="height:80px;">

            </div>
            <h1>Project Information</h1>
            <p>This project was developed as part of a <strong>Cyber Security Internship</strong>. This project is designed to <strong>Secure the Organizations in Real World from Cyber Frauds performed by Hackers</strong>.</p>
            <table>
                <tr><th>Project Details</th><th>Value</th></tr>
                <tr><td>Project Name</td><td>Password Strength Checker</td></tr>
                <tr><td>Project Description</td><td>Developing Password Strength Checker to know the Strength of the Passwords to avoid Cyber Attacks</td></tr>
                <tr><td>Project Start Date</td><td>10-JULY-2025</td></tr>
                <tr><td>Project End Date</td><td>5-AUG-2025</td></tr>
                <tr><td>Project Status</td><td><strong>Completed</strong></td></tr>
            </table>

            <h2>Developer Details</h2>
            <table>
                <tr><th>Name</th><th>Employee ID</th><th>Email</th></tr>
                <tr><td>Vaishnavi Samala</td><td>ST#IS#7417</td><td>samalavaish77@gmail.com</td></tr>
                <tr><td>B.S.S.Sarveni</td><td>ST#IS#7419</td><td>seshasai116@gmail.com</td></tr>
                <tr><td>S.Prem Kumar</td><td>ST#IS#7427</td><td>premk45917@gmail.com</td></tr>
                <tr><td>Prasanna Agulla</td><td>ST#IS#7415</td><td>saikiranfor875@gmail.com</td></tr>
            </table>

            <h2>Company Details</h2>
            <table>
                <tr><th>Company</th><th>Value</th></tr>
                <tr><td>Name</td><td>Supraja Technologies</td></tr>
            </table> 

            <h2>Contact Information</h2>
            <table>
                <tr><th>Category</th><th>Details</th></tr>
                <tr><td>Email</td><td><a href="mailto:contact@suprajatechnologies.com">contact@suprajatechnologies.com</a></td></tr>
                <tr><td>Website</td><td><a href="https://www.suprajatechnologies.com" target="_blank">suprajatechnologies.com</a></td></tr>
            </table>

            <div class="footer">
                &copy; 2025 Supraja Technologies. All rights reserved.
            </div>
        </div>
    </body>
    </html>
    """
    try:
        with tempfile.NamedTemporaryFile("w", delete=False, suffix=".html", encoding="utf-8") as f:
            f.write(html_code)
            path = f.name
        webbrowser.open("file://" + os.path.realpath(path))
    except Exception as e:
        messagebox.showerror("Error", f"Could not open project info: {e}")

# -------------------- Steganography helpers --------------------
def _embed_bytes_in_image(cover_path, data_bytes, out_path):
    """Embed bytes into cover image LSBs and save PNG to out_path."""
    image = Image.open(cover_path).convert("RGB")
    width, height = image.size

    binary_data = "".join(format(byte, "08b") for byte in data_bytes) + DELIMITER
    if len(binary_data) > width * height * 3:
        raise ValueError("Message is too long for this image. Choose a larger image or shorter message.")

    encoded_image = image.copy()
    pixels = encoded_image.load()

    data_index = 0
    done = False
    for y in range(height):
        for x in range(width):
            if data_index >= len(binary_data):
                done = True
                break
            r, g, b = image.getpixel((x, y))

            r = (r & ~1) | int(binary_data[data_index]); data_index += 1
            if data_index < len(binary_data):
                g = (g & ~1) | int(binary_data[data_index]); data_index += 1
            if data_index < len(binary_data):
                b = (b & ~1) | int(binary_data[data_index]); data_index += 1

            pixels[x, y] = (r, g, b)
        if done:
            break

    encoded_image.save(out_path, "PNG")

def _extract_bytes_from_image(stego_path):
    """Extract bytes from an image's LSBs until DELIMITER."""
    image = Image.open(stego_path).convert("RGB")
    width, height = image.size

    binary_data = ""
    found = False
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            binary_data += str(r & 1) + str(g & 1) + str(b & 1)
            if DELIMITER in binary_data:
                found = True
                break
        if found:
            break

    if not found:
        raise ValueError("No hidden message delimiter found in this image.")

    payload_bits = binary_data.split(DELIMITER)[0]
    secret_bytes = bytearray(int(payload_bits[i:i+8], 2) for i in range(0, len(payload_bits), 8))
    return bytes(secret_bytes)

# -------------------- Main App --------------------
class StegApp:
    def __init__(self, root):
        self.root = root
        root.title("Image Steganography")
        root.geometry("920x760")
        root.configure(bg="#0f172a")
        root.resizable(False, False)

        # Global formal font
        root.option_add("*Font", "Georgia 11")
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Georgia", 11, "bold"), padding=8)

        # Header (logo + title)
        header = tk.Frame(root, bg="#0f172a")
        header.pack(pady=(12, 6), fill="x")

        left = tk.Frame(header, bg="#0f172a")
        left.pack(side="left", padx=16)
        try:
            logo = Image.open(LOGO_PATH)
            logo.thumbnail((90, 90))
            self.logo_tk = ImageTk.PhotoImage(logo)
            tk.Label(left, image=self.logo_tk, bg="#0f172a").pack()
        except Exception:
            tk.Label(left, text="[Logo]", bg="#0f172a", fg="white", font=("Georgia", 10, "bold")).pack()

        tk.Label(header, text="Image Steganography", font=("Georgia", 26, "bold"), fg="#facc15", bg="#0f172a").pack(side="left", padx=12)

        # Top controls
        top_frame = tk.Frame(root, bg="#0f172a")
        top_frame.pack(pady=8, padx=16, fill="x")

        ttk.Button(top_frame, text="Project Info", command=project_info).pack(side="left")
        ttk.Button(top_frame, text="Quit", command=root.quit).pack(side="right")

        # Main area
        main_frame = tk.Frame(root, bg="#0f172a")
        main_frame.pack(padx=16, pady=6, fill="both", expand=True)

        # Preview card
        preview_card = tk.LabelFrame(main_frame, text="Image Preview", bg="#0b1220", fg="white", font=("Georgia", 10, "bold"))
        preview_card.place(x=16, y=10, width=620, height=600)

        self.preview_label = tk.Label(preview_card, text="No image selected", bg="#0b1220", fg="#94a3b8")
        self.preview_label.pack(expand=True)

        # Controls card (note: removed display of LOGO_PATH)
        controls_card = tk.LabelFrame(main_frame, text="Actions & Settings", bg="#0b1220", fg="white", font=("Georgia", 10, "bold"))
        controls_card.place(x=660, y=10, width=240, height=600)

        ttk.Button(controls_card, text="Choose Image", command=self.choose_image).pack(pady=(12, 8), padx=12, fill="x")
        ttk.Button(controls_card, text="Open Hide Window", command=self.open_hide_window).pack(pady=8, padx=12, fill="x")
        ttk.Button(controls_card, text="Open Extract Window", command=self.open_extract_window).pack(pady=8, padx=12, fill="x")

        # Tip text remains, but icon path is not shown
        tk.Label(controls_card, text="Tip: Use PNG images (lossless) for reliable results. For Gmail, use an App Password or enable appropriate SMTP access.", bg="#0b1220", fg="#cbd5e1", wraplength=220, justify="left").pack(padx=12, pady=(14,2))

        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = tk.Label(root, textvariable=self.status_var, anchor="w", bg="#071027", fg="lightgray")
        status_bar.pack(side="bottom", fill="x")

        self.current_image_path = None

    def set_status(self, text):
        self.status_var.set(text)

    def choose_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if not path:
            return
        self.current_image_path = path
        img = Image.open(path)
        img.thumbnail((600, 600))
        img_tk = ImageTk.PhotoImage(img)
        self.preview_label.configure(image=img_tk, text="")
        self.preview_label.image = img_tk
        self.set_status(f"Loaded: {os.path.basename(path)}")

    def open_hide_window(self):
        if not self.current_image_path:
            messagebox.showwarning("No Image", "Please choose a cover image first from the main window.")
            return

        win = tk.Toplevel(self.root)
        win.title("Hide Text into Image")
      

        frame = tk.Frame(win, padx=12, pady=12, bg="#eef2ff")
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Cover Image:", anchor="w", bg="#eef2ff").grid(row=0, column=0, sticky="w")
        cover_entry = tk.Entry(frame, width=56)
        cover_entry.grid(row=0, column=1, pady=6, padx=6)
        cover_entry.insert(0, self.current_image_path)

        def browse_cover():
            p = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
            if p:
                cover_entry.delete(0, tk.END)
                cover_entry.insert(0, p)

        ttk.Button(frame, text="Browse", command=browse_cover).grid(row=0, column=2, padx=4)

        tk.Label(frame, text="Message to hide:", anchor="w", bg="#eef2ff").grid(row=1, column=0, sticky="nw", pady=(8,0))
        message_text = tk.Text(frame, width=56, height=8)
        message_text.grid(row=1, column=1, columnspan=2, pady=6, padx=6)

        tk.Label(frame, text="Sender Email:", anchor="w", bg="#eef2ff").grid(row=2, column=0, sticky="w")
        sender_entry = tk.Entry(frame, width=56)
        sender_entry.grid(row=2, column=1, pady=6, padx=6)

        tk.Label(frame, text="SMTP Password (or App Password):", anchor="w", bg="#eef2ff").grid(row=3, column=0, sticky="w")
        pwd_entry = tk.Entry(frame, width=56, show="*")
        pwd_entry.grid(row=3, column=1, pady=6, padx=6)

        tk.Label(frame, text="Receiver Email:", anchor="w", bg="#eef2ff").grid(row=4, column=0, sticky="w")
        receiver_entry = tk.Entry(frame, width=56)
        receiver_entry.grid(row=4, column=1, pady=6, padx=6)

        def do_hide():
            cover = cover_entry.get().strip()
            message = message_text.get("1.0", "end").strip()
            sender = sender_entry.get().strip()
            pwd = pwd_entry.get().strip()
            receiver = receiver_entry.get().strip()

            if not all([cover, message, sender, pwd, receiver]):
                messagebox.showwarning("Missing data", "All fields are required.")
                return

            try:
                # encrypt payload
                key = Fernet.generate_key()
                fernet = Fernet(key)
                payload = f"SECRET_MSG::{message}".encode("utf-8")
                encrypted = fernet.encrypt(payload)

                base, ext = os.path.splitext(cover)
                out_path = base + "_stego.png"

                # embed encrypted bytes
                _embed_bytes_in_image(cover, encrypted, out_path)

                # prepare email with key and attachment
                msg = MIMEMultipart()
                msg["From"] = sender
                msg["To"] = receiver
                msg["Subject"] = "Image with hidden message and key"
                body = f"Hello,\n\nAttached is the image with a hidden message. Use this key to extract: {key.decode()}\n\n-- Auto-generated by Image Steg App"
                msg.attach(MIMEText(body, "plain"))

                with open(out_path, "rb") as f:
                    part = MIMEApplication(f.read(), Name=os.path.basename(out_path))
                    part["Content-Disposition"] = f'attachment; filename="{os.path.basename(out_path)}"'
                    msg.attach(part)

                server = smtplib.SMTP("smtp.gmail.com", 587, timeout=20)
                server.starttls()
                server.login(sender, pwd)
                server.send_message(msg)
                server.quit()

                messagebox.showinfo("Success", f"Message hidden and sent! Output: {out_path}\n\nKey (copy it from this message and keep it safe):\n{key.decode()}")
                win.destroy()
                self.set_status("Hide: Completed")

            except Exception as e:
                messagebox.showerror("Error", f"Failed to hide/send: {e}")
                self.set_status("Error during hide")

        # Big, visible button at the bottom
        send_btn = tk.Button(frame, text="Hide & Send Email", bg="#facc15", fg="black",
                             font=("Georgia", 12, "bold"), command=do_hide)
        send_btn.grid(row=6, column=0, columnspan=3, pady=18, ipadx=10, ipady=6)

    def open_extract_window(self):
        win = tk.Toplevel(self.root)
        win.title("Extract Text from Image")
    

        frame = tk.Frame(win, padx=12, pady=12)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Stego Image:", anchor="w").grid(row=0, column=0, sticky="w")
        file_entry = tk.Entry(frame, width=50)
        file_entry.grid(row=0, column=1, pady=6, padx=6)

        def browse_file():
            p = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if p:
                file_entry.delete(0, tk.END)
                file_entry.insert(0, p)

        ttk.Button(frame, text="Browse", command=browse_file).grid(row=0, column=2, padx=4)

        tk.Label(frame, text="Decryption Key:", anchor="w").grid(row=1, column=0, sticky="w")
        key_entry = tk.Entry(frame, width=50, show="*")
        key_entry.grid(row=1, column=1, pady=6, padx=6)

        def do_extract():
            path = file_entry.get().strip()
            key_text = key_entry.get().strip()
            if not path or not key_text:
                messagebox.showwarning("Missing data", "Both fields are required.")
                return

            try:
                secret_bytes = _extract_bytes_from_image(path)
                fernet = Fernet(key_text.encode())
                decrypted = fernet.decrypt(secret_bytes)
                decoded = decrypted.decode("utf-8")
                if decoded.startswith("SECRET_MSG::"):
                    messagebox.showinfo("Secret Message", decoded.split("::", 1)[1])
                    self.set_status("Extract: Success")
                else:
                    messagebox.showerror("Error", "Hidden data found but format is invalid.")
                    self.set_status("Extract: Invalid format")

            except InvalidToken:
                messagebox.showerror("Decryption error", "Wrong key or corrupted data (InvalidToken).")
                self.set_status("Extract: Invalid token")
            except Exception as e:
                messagebox.showerror("Error", f"Extraction failed: {e}")
                self.set_status("Extract: Error")

        # Add Extract button (visible)
        extract_btn = tk.Button(frame, text="Extract", bg="#facc15", fg="black",
                                font=("Georgia", 12, "bold"), command=do_extract)
        extract_btn.grid(row=2, column=0, columnspan=3, pady=18, ipadx=10, ipady=6)

# -------------------- Run --------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = StegApp(root)
    root.mainloop()
