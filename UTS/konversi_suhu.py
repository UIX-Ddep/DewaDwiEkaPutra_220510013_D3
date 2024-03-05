from tkinter import *
import tkinter.font

root = Tk()
root.title("tempconverter")
root.geometry("400x200")
root.resizable(False,False)

# mengatur ukuran font
thefont = tkinter.font.Font(size=15)

# membuat sebuah frame baru
nwframe = LabelFrame(root,text="temp converter",padx=10,pady=10)
nwframe.place(x =15 , y = 10 )

# judul dan tulisan samadengan 
judul = Label(nwframe,text="Temperatur").grid(row = 0, columnspan=3)
samde = Label(nwframe, text="=").grid(row = 1,column=1)

# membuat kotak input nomor
e1 = Entry(nwframe,width=15)
e2 = Entry(nwframe,width=15)
e1["font"] = thefont
e2["font"] = thefont
e2.insert(0, "0")
e1.grid(row=1,column=0)
e2.grid(row=1, column=2)

# menuliskan rumus dan semua fungsi
rmslbl = Label(nwframe,text="Formula",bg="yellow")
rmslbl.place(x = 1, y =90)

rmsnya = Label(nwframe,text="(...°C x 9/5) + 32 = ... °F")
rmsnya.place(x = 50 , y = 90)

chek = {"rumus","yes"}

def rumus(rm):
    # hapus tulisan pada kotak 2
    e2.delete(0,END)
    
    # mendapatkan nilai dari kotak
    kotaksatu = cliked.get()
    kotakdua = cliked2.get()
    nomer1 = int(e1.get())

    # menghilangkan tulisan sebelumnya 
    global rmsnya
    if "rumus" in chek:
        rmsnya.place_forget()
    else:
        pass
      
    # menuliskan rumus dan menentukan hitungan
    if kotaksatu == "celcius" and kotakdua == "fahrentheit":
        rmsnya = Label(nwframe,text="("+e1.get()+"°C × 9/5) + 32 = ... °F")
        hitungan = (nomer1 * 9/5) + 32
    elif kotaksatu == "celcius" and kotakdua == "kelvin":
        rmsnya = Label(nwframe,text=e1.get()+"°C + 273.15 = ... K")
        hitungan = (nomer1 + 273.15)
    elif kotaksatu == "celcius" and kotakdua == "reamur":
        rmsnya = Label(nwframe,text="(4/5 × "+e1.get()+"°C) = ... R")
        hitungan = (4/5 * nomer1)
    elif kotaksatu == "fahrentheit" and kotakdua == "celcius":
        rmsnya = Label(nwframe,text="("+e1.get()+"°F - 32) × 5/9 = ... °C")
        hitungan = (nomer1 - 32) * 5/9
    elif kotaksatu == "fahrentheit" and kotakdua == "kelvin":
        rmsnya = Label(nwframe,text="("+e1.get()+"°F - 32) × 5/9 + 273.15 = ... K")
        hitungan = (nomer1 - 32) * 5/9 + 273.15
    elif kotaksatu == "fahrentheit" and kotakdua == "reamur":
        rmsnya = Label(nwframe,text="("+e1.get()+"F - 32) × 4/9 = ... R")
        hitungan = (nomer1 - 32) * 4/9
    elif kotaksatu == "reamur" and kotakdua == "celcius":
        rmsnya = Label(nwframe,text="5/4 × "+e1.get()+"R) = ... °C")
        hitungan = (5/4 * nomer1)
    elif kotaksatu == "reamur" and kotakdua == "fahrentheit":
        rmsnya = Label(nwframe,text="(9/4 × "+e1.get()+"R) + 32 = ... F")
        hitungan = (9/4 * nomer1) + 32
    elif kotaksatu == "reamur" and kotakdua == "kelvin":
        rmsnya = Label(nwframe,text="(5/4 ×"+e1.get()+"R) + 273 = ... K")
        hitungan = (5/4 * nomer1) + 273
    elif kotaksatu == "kelvin" and kotakdua == "celcius":
        rmsnya = Label(nwframe,text=e1.get()+"K - 273.15 = ... °C")
        hitungan = (nomer1 - 273.15)
    elif kotaksatu == "kelvin" and kotakdua == "fahrentheit":
        rmsnya = Label(nwframe,text="("+e1.get()+"K - 273.15) × 9/5 + 32 = ... °F ")
        hitungan = (nomer1 - 273.15) * 9/5 + 32 
    elif kotaksatu == "kelvin" and kotakdua == "reamur":
        rmsnya = Label(nwframe,text="("+e1.get()+"k - 273) × 4/5 = ... R")
        hitungan = (nomer1 - 273) * 4/5
    elif kotaksatu == "celcius" and kotakdua == "celcius" or kotaksatu == "fahrentheit" and kotakdua == "fahrentheit" or  kotaksatu == "reamur" and kotakdua == "reamur" or kotaksatu == "kelvin" and kotakdua == "kelvin" :
        rmsnya = Label(nwframe,text="tidak ada rumus")
        hitungan = nomer1
    hasil = hitungan
    e2.insert(0,hasil)
    rmsnya.place(x = 50 , y = 90)
    




# memasukkan nilai untuk membuat pilihan temperatur
option = ["celcius","fahrentheit","kelvin","reamur"]
cliked = StringVar()
cliked.set(option[0])
drop = OptionMenu(nwframe,cliked,*option,command=rumus)
drop.config(width=20)
drop.grid(row = 2,column=0)

cliked2 = StringVar()
cliked2.set(option[1])
drop2 = OptionMenu(nwframe,cliked2,*option,command=rumus)
drop2.config(width=20)
drop2.grid(row = 2,column=2)

#membuat tombol menghitung
btn = Button(nwframe,text="count",command=lambda:rumus("hitung"))
btn.grid(row = 3,column=2)



root.mainloop()