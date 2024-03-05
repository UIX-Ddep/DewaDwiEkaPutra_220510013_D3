import tkinter as tk
from tkinter import ttk
from googletrans import Translator

def translate_text():
    text_to_translate = entry.get()
    selected_language = destination_language.get()
    translator = Translator()
    translated_text = translator.translate(text_to_translate, dest=selected_language)
    translated_box.delete(1.0, tk.END)  # Menghapus hasil sebelumnya
    translated_box.insert(tk.END, translated_text.text)

# Membuat GUI
root = tk.Tk()
root.title("Aplikasi Translator")
root.resizable(width=False, height=False)

# Mengatur warna background
root.configure(bg="#FFF7D4")  # Ganti dengan warna latar belakang yang diinginkan

# Menambahkan style untuk tombol
style = ttk.Style()
style.configure("TButton", foreground="white", background="#4CAF50")  # Ganti dengan warna font dan latar belakang tombol yang diinginkan

label = tk.Label(root, text="Masukkan Teks:", bg="#EFEFEF", fg="black", font=("Arial", 12))  # Ganti dengan warna font, latar belakang, dan font yang diinginkan
label.pack(pady=(10, 5))

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=(0, 5))

destination_language_label = tk.Label(root, text="Pilih Bahasa Tujuan:", bg="#EFEFEF", fg="black", font=("Arial", 12))  # Ganti dengan warna font, latar belakang, dan font yang diinginkan
destination_language_label.pack(pady=(0, 5))

# Menambahkan pilihan bahasa
languages = ['en', 'id', 'pt', 'ro']  # Kode bahasa yang akan ditampilkan
destination_language = ttk.Combobox(root, values=languages, state="readonly", font=("Calibri", 12))
destination_language.pack(pady=(0, 5))

translate_button = tk.Button(root, text="Translate", command=translate_text, font=("Calibri", 12), bg="#5C8374", fg="white")  # Ganti dengan warna font, latar belakang, dan warna tombol yang diinginkan
translate_button.pack(pady=(10, 5))

# Mengatur wrap pada kolom teks untuk mengikuti panjang teks
translated_box = tk.Text(root, height=6, width=30, wrap=tk.WORD, font=("Calibri", 12))
translated_box.pack(pady=(0, 10))

root.geometry("400x400")  # Atur ukuran window secara manual
root.resizable(False,False)
root.mainloop()

