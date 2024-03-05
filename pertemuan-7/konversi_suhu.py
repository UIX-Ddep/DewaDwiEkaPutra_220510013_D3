import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        # Ambil nilai dari inputan pengguna
        input_temperature = float(entry_temperature.get())

        # Ambil jenis suhu yang dipilih
        input_scale = combo_from.get()
        output_scale = combo_to.get()

        # Lakukan konversi suhu
        if input_scale == "Celsius" and output_scale == "Fahrenheit":
            result = (input_temperature * 9/5) + 32
        elif input_scale == "Celsius" and output_scale == "Kelvin":
            result = input_temperature + 273
        elif input_scale == "Celsius" and output_scale == "Reamur":
            result = input_temperature * 4/5        
        elif input_scale == "Fahrenheit" and output_scale == "Celsius":
            result = (input_temperature - 32) * 5/9
        elif input_scale == "Fahrenheit" and output_scale == "Kelvin":
            result = (input_temperature - 32) * 5/9 + 273
        elif input_scale == "Fahrenheit" and output_scale == "Reamur":
            result = (input_temperature - 32) * 4/9            
        elif input_scale == "Kelvin" and output_scale == "Celsius":
            result = input_temperature - 273
        elif input_scale == "Kelvin" and output_scale == "Fahrenheit":
            result = (input_temperature - 273) * 9/5 + 32
        elif input_scale == "Kelvin" and output_scale == "Reamur":
            result = (input_temperature - 273) * 4/5
        elif input_scale == "Reamur" and output_scale == "Celsius":
            result = 5/4 * input_temperature
        elif input_scale == "Reamur" and output_scale == "Fahrenheit":
            result = (9/4 * input_temperature) + 32
        elif input_scale == "Reamur" and output_scale == "Kelvin":
            result = 5/4 * input_temperature + 273
        else:
            result = input_temperature  # Jika jenis suhu sama, hasilnya tetap

        # Update label dengan hasil konversi
        label_result.config(text=f"Result: {result:.2f} {output_scale}")

    except ValueError:
        # Tangani jika pengguna memasukkan sesuatu yang bukan angka
        label_result.config(text="Please enter a valid temperature")

# Buat instance dari Tkinter
root = tk.Tk()
root.title("Temperature Converter")

# Mengatur warna background
root.configure(bg="#1E1E1E")  # Ganti dengan warna latar belakang yang diinginkan

# Buat label untuk input suhu
label_temperature = tk.Label(root, text="Enter Temperature:", bg="#1E1E1E", fg="white")  # Ganti dengan warna font dan latar belakang yang diinginkan
label_temperature.pack(pady=10)

# Buat entry untuk memasukkan suhu
entry_temperature = tk.Entry(root)
entry_temperature.pack(pady=10)

# Buat label untuk memilih jenis suhu dari
label_from = tk.Label(root, text="From:", bg="#1E1E1E", fg="white")  # Ganti dengan warna font dan latar belakang yang diinginkan
label_from.pack()

# Buat dropdown untuk memilih jenis suhu dari
options = ["Celsius", "Fahrenheit", "Kelvin", "Reamur"]
combo_from = tk.StringVar()
combo_from.set(options[0])  # Set default value
dropdown_from = ttk.Combobox(root, textvariable=combo_from, values=options)
dropdown_from.pack(pady=10)

# Buat label untuk memilih jenis suhu ke
label_to = tk.Label(root, text="To:", bg="#1E1E1E", fg="white")  # Ganti dengan warna font dan latar belakang yang diinginkan
label_to.pack()

# Buat dropdown untuk memilih jenis suhu ke
combo_to = tk.StringVar()
combo_to.set(options[1])  # Set default value
dropdown_to = ttk.Combobox(root, textvariable=combo_to, values=options)
dropdown_to.pack(pady=10)

# Buat tombol konversi suhu
button_convert = tk.Button(root, text="Convert", command=convert_temperature, bg="#4CAF50", fg="white")  # Ganti dengan warna font, latar belakang, dan warna tombol yang diinginkan
button_convert.pack(pady=20)

# Buat label untuk menampilkan hasil konversi
label_result = tk.Label(root, text="Result:", bg="#1E1E1E", fg="white")  # Ganti dengan warna font dan latar belakang yang diinginkan
label_result.pack()

# Jalankan aplikasi Tkinter
root.mainloop()
