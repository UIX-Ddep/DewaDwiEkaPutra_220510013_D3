import tkinter as tk
import math

def kalkulator():
    try:
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())
        tinggi_limas = float(entry_tinggi_limas.get())
        tinggi_alas = float(entry_tinggi_alas.get())

        volume = (panjang * lebar * tinggi_limas) / 3
        luas_permukaan = (panjang * lebar) + (panjang * math.sqrt((lebar/2)** 2 + tinggi_alas** 2)) + (lebar * math.sqrt((panjang/2)**2 + tinggi_alas**2))
        
        label_volume.config(text="Volume Limas Segi Empat: {:.2f}".format(volume))
        label_luas_permukaan.config(text="Luas Permukaan Limas Segi Empat: {:.2f}".format(luas_permukaan))
    except ValueError:
        label_volume.config(text="Masukkan bilangan valid")
        label_luas_permukaan.config(text="")

window = tk.Tk()
window.title("Kalkulator Limas Segi Empat")
window.geometry("300x350")

label_panjang = tk.Label(window, text="Panjang:")
label_panjang.pack()
entry_panjang = tk.Entry(window)
entry_panjang.pack(padx=5,pady=5)

label_lebar = tk.Label(window, text="Lebar:")
label_lebar.pack()
entry_lebar = tk.Entry(window)
entry_lebar.pack(padx=5,pady=5)

label_tinggi_limas = tk.Label(window, text="Tinggi Limas:")
label_tinggi_limas.pack()
entry_tinggi_limas = tk.Entry(window)
entry_tinggi_limas.pack(padx=5,pady=5)

label_tinggi_alas = tk.Label(window, text="Tinggi Alas:")
label_tinggi_alas.pack()
entry_tinggi_alas = tk.Entry(window)
entry_tinggi_alas.pack(padx=5,pady=5)

calculate_button = tk.Button(window, text="Hitung", command=kalkulator)
calculate_button.pack(padx=12,pady=12)

label_volume = tk.Label(window, text="")
label_volume.pack(padx=10,pady=6)
label_luas_permukaan = tk.Label(window, text="")
label_luas_permukaan.pack(padx=10,pady=6)

window.mainloop()