import tkinter as tk
import math

def kalkulator():
    try:
        alas = float(entry_alas.get())
        tinggi_segitiga = float(entry_tinggi_segitiga.get())
        tinggi_limas = float(entry_tinggi_limas.get())

        volume = (alas * tinggi_segitiga * tinggi_limas)/3
        luas_permukaan = (alas * tinggi_segitiga) + (3 * (alas * tinggi_limas)/2)
        
        label_volume.config(text="Volume Limas Segi Empat: {:.2f}".format(volume))
        label_luas_permukaan.config(text="Luas Permukaan Limas Segi Empat: {:.2f}".format(luas_permukaan))
    except ValueError:
        label_volume.config(text="Masukkan bilangan valid")
        label_luas_permukaan.config(text="")

window = tk.Tk()
window.title("Kalkulator Limas Segi Tiga")
window.geometry("300x350")

label_alas = tk.Label(window, text="Alas:")
label_alas.pack()
entry_alas = tk.Entry(window)
entry_alas.pack(padx=5,pady=5)

label_tinggi_segitiga = tk.Label(window, text="Tinggi Segitiga:")
label_tinggi_segitiga.pack()
entry_tinggi_segitiga = tk.Entry(window)
entry_tinggi_segitiga.pack(padx=5,pady=5)

label_tinggi_limas = tk.Label(window, text="Tinggi Limas:")
label_tinggi_limas.pack()
entry_tinggi_limas = tk.Entry(window)
entry_tinggi_limas.pack(padx=5,pady=5)



calculate_button = tk.Button(window, text="Hitung", command=kalkulator)
calculate_button.pack(padx=12,pady=12)

label_volume = tk.Label(window, text="")
label_volume.pack(padx=10,pady=6)
label_luas_permukaan = tk.Label(window, text="")
label_luas_permukaan.pack(padx=10,pady=6)

window.mainloop()