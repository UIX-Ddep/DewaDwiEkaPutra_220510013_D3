import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

def get_celcius():
    suhu = txtsuhu.get()
    C = (5/9) * (float(suhu) - 32)
    txtCelcius.delete(0, END)
    txtCelcius.insert(END, C)

def get_reamur():
    suhu = txtsuhu.get()
    R = (4/9) * (float(suhu) - 32)
    txtReamur.delete(0, END)
    txtReamur.insert(END, R)

def get_kelvin():
    suhu = txtsuhu.get()
    K = (5/9) * (float(suhu) - 32) + 273
    txtKelvin.delete(0, END)
    txtKelvin.insert(END, K)

def hitung():
    get_celcius()
    get_reamur()
    get_kelvin()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Suhu Fahrenheit")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label
suhu = Label(frame, text="Fahrenheit:")
suhu.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Textbox
txtsuhu = Entry(frame)
txtsuhu.grid(row=0, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

C = Label(frame, text="Celcius:")
C.grid(row=3, column=0, sticky=W, padx=5, pady=5)

R = Label(frame, text="Reamur:")
R.grid(row=4, column=0, sticky=W, padx=5, pady=5)

K = Label(frame, text="Kelvin:")
K.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox
txtCelcius = Entry(frame)
txtCelcius.grid(row=3, column=1, sticky=W, padx=5, pady=5)

txtReamur = Entry(frame)
txtReamur.grid(row=4, column=1, sticky=W, padx=5, pady=5)

txtKelvin = Entry(frame)
txtKelvin.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
