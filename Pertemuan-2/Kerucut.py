import tkinter as tk
import math

def kalkulator():
    try:
        jari_jari = float(entry_jari_jari.get())
        tinggi = float(entry_tinggi.get())
        volume = (1/3) * math.pi * (jari_jari ** 2) * tinggi
        luas_permukaan = math.pi * jari_jari * (jari_jari + math.sqrt ((jari_jari ** 2) + (tinggi ** 2)))
        label_volume.config(text="Volume Kerucut: {:.2f}".format(volume))
        label_luas_permukaan.config(text="Luas Permukaan kerucut: {:.2f}".format(luas_permukaan))
    except ValueError:
        label_volume.config(text="Masukkan bilangan valid")
        label_luas_permukaan.config(text="")

window = tk.Tk()
window.title("Kalkulator Kerucut")
window.geometry("300x300")

label_jari_jari = tk.Label(window, text="Jari Jari:")
label_jari_jari.pack()
entry_jari_jari = tk.Entry(window)
entry_jari_jari.pack(padx=5,pady=5)

label_tinggi = tk.Label(window, text="Tinggi:")
label_tinggi.pack()
entry_tinggi = tk.Entry(window)
entry_tinggi.pack(padx=5,pady=5)

calculate_button = tk.Button(window, text="Hitung", command=kalkulator)
calculate_button.pack(padx=12,pady=12)

label_volume = tk.Label(window, text="")
label_volume.pack(padx=10,pady=6)
label_luas_permukaan = tk.Label(window, text="")
label_luas_permukaan.pack(padx=10,pady=6)

window.mainloop()