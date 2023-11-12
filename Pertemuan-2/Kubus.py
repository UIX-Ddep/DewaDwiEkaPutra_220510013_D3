import tkinter as tk

def kalkulator():
    try:
        sisi = float(entry_sisi.get())
        volume = sisi**3
        luas_permukaan = 6 * (sisi **2) 
        label_volume.config(text="Volume Kubus: {:.2f}".format(volume))
        label_luas_permukaan.config(text="Luas Permukaan kubus: {:.2f}".format(luas_permukaan))
    except ValueError:
        label_volume.config(text="Masukkan bilangan valid")
        label_luas_permukaan.config(text="")

window = tk.Tk()
window.title("Kalkulator Kubus")
window.geometry("300x300")

label_sisi = tk.Label(window, text="Sisi:")
label_sisi.pack()
entry_sisi = tk.Entry(window)
entry_sisi.pack(padx=5,pady=5)

calculate_button = tk.Button(window, text="Hitung", command=kalkulator)
calculate_button.pack(padx=12,pady=12)

label_volume = tk.Label(window, text="")
label_volume.pack(padx=10,pady=6)
label_luas_permukaan = tk.Label(window, text="")
label_luas_permukaan.pack(padx=10,pady=6)

window.mainloop()