import tkinter as tk
import math

def kalkulator():
    try:
        alas = float(entry_alas.get())
        tinggi_segitiga = float(entry_tinggi_segitiga.get())
        tinggi_prisma = float(entry_tinggi_prisma.get())
        panjang_sisi = float(entry_panjang_sisi.get())

        volume = (alas * tinggi_segitiga * tinggi_prisma) /2
        luas_permukaan = (alas * tinggi_segitiga) + (3 * panjang_sisi * tinggi_prisma) 

        label_volume.config(text="Volume Prisma Segitiga: {:.2f}".format(volume))
        label_luas_permukaan.config(text="Luas Permukaan Prisma Segitiga: {:.2f}".format(luas_permukaan))
    except ValueError:
        label_volume.config(text="Masukkan bilangan valid")
        label_luas_permukaan.config(text="")

window = tk.Tk()
window.title("Kalkulator Prisma Segitiga")
window.geometry("300x400")

label_alas = tk.Label(window, text="Alas:")
label_alas.pack()
entry_alas = tk.Entry(window)
entry_alas.pack(padx=5,pady=5)  

label_tinggi_segitiga = tk.Label(window, text="Tinggi Segitiga:")
label_tinggi_segitiga.pack()
entry_tinggi_segitiga = tk.Entry(window)
entry_tinggi_segitiga.pack(padx=5,pady=5)

label_tinggi_prisma = tk.Label(window, text="Tinggi Prisma:")
label_tinggi_prisma.pack()
entry_tinggi_prisma= tk.Entry(window)
entry_tinggi_prisma.pack(padx=5,pady=5)

label_panjang_sisi = tk.Label(window, text="Panjang Sisi:")
label_panjang_sisi.pack()
entry_panjang_sisi = tk.Entry(window)
entry_panjang_sisi.pack(padx=5,pady=5)

calculate_button = tk.Button(window, text="Hitung", command=kalkulator)
calculate_button.pack(padx=12,pady=12)

label_volume = tk.Label(window, text="")
label_volume.pack(padx=10,pady=6)
label_luas_permukaan = tk.Label(window, text="")
label_luas_permukaan.pack(padx=10,pady=6)

window.mainloop()