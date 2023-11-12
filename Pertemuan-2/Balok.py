import tkinter as tk

def kalkulator():
    try:
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())
        tinggi = float(entry_tinggi.get())
        volume = panjang * lebar * tinggi
        luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
        label_volume.config(text="Volume Balok: {:.2f}".format(volume))
        label_luas_permukaan.config(text="Luas Permukaan Balok: {:.2f}".format(luas_permukaan))
    except ValueError:
        label_volume.config(text="Masukkan bilangan valid")
        label_luas_permukaan.config(text="")

window = tk.Tk()
window.title("Kalkulator Balok")
window.geometry("300x300")


label_panjang = tk.Label(window, text="Panjang Balok:")
label_panjang.pack()
entry_panjang = tk.Entry(window)
entry_panjang.pack(padx=5,pady=5)

label_lebar = tk.Label(window, text="Lebar Balok:")
label_lebar.pack()
entry_lebar = tk.Entry(window)
entry_lebar.pack(padx=5,pady=5)

label_tinggi = tk.Label(window, text="Tinggi Balok:")
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