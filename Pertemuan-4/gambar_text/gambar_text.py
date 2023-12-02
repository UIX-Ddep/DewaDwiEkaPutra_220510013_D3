import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

# Set the path to the Tesseract executable (replace with your actual path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        display_image(file_path)
        result_text = image_to_text(file_path)
        result_var.set(result_text)

def display_image(image_path):
    img = Image.open(image_path)
    img.thumbnail((300, 300))  # Resize the image for display
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img  # Keep a reference to the image to prevent garbage collection

# Create the main Tkinter window
root = tk.Tk()
root.title("Image to Text Converter")

# Create and configure widgets
browse_button = tk.Button(root, text="Browse Image", command=browse_image)
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, wraplength=400, justify='left')
image_label = tk.Label(root)

# Place widgets in the window
browse_button.pack(pady=10)
image_label.pack(pady=10)
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
