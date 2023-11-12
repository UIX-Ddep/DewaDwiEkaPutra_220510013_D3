import tkinter as tk
import math

def kalkulator():
    try:
        jari_jari = float(entry_jari_jari.get())
        volume = (4/3)* math.pi * (jari_jari ** 3)
        luas_permukaan = 4 * math.pi * (jari_jari ** 2)
        label_volume.config(text="Volume Bola: {:.2f}".format(volume))
        label_luas_permukaan.config(text="Luas Permukaan Bola: {:.2f}".format(luas_permukaan))
    except ValueError:
        label_volume.config(text="Masukkan bilangan valid")
        label_luas_permukaan.config(text="")

window = tk.Tk()
window.title("Kalkulator Bola")
window.geometry("300x300")

label_jari_jari = tk.Label(window, text="Jari-Jari:")
label_jari_jari.pack()
entry_jari_jari = tk.Entry(window)
entry_jari_jari.pack(padx=5,pady=5)

calculate_button = tk.Button(window, text="Hitung", command=kalkulator)
calculate_button.pack(padx=12,pady=12)

label_volume = tk.Label(window, text="")
label_volume.pack(padx=10,pady=6)
label_luas_permukaan = tk.Label(window, text="")
label_luas_permukaan.pack(padx=10,pady=6)

window.mainloop()