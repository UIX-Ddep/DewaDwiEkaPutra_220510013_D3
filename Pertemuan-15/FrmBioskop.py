import tkinter as tk
from tkinter import ttk, messagebox, StringVar
from Bioskop import Bioskop

class FrmBioskop:
    
    def __init__(self, parent, title, update_main_window):
        self.parent = parent       
        self.parent.geometry("620x500")
        self.parent.title(title)
        self.update_main_window = update_main_window 
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = ttk.Frame(self.parent, borderwidth=10)  # Use 'borderwidth' instead of 'bd'
        mainFrame.pack(fill=tk.BOTH, expand=tk.YES)
        
        # Label
        ttk.Label(mainFrame, text='No Transaksi:').grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtNoTransaksi = ttk.Entry(mainFrame) 
        self.txtNoTransaksi.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNoTransaksi.bind("<Return>", self.onCari)

        ttk.Label(mainFrame, text='Nama :').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtNama = ttk.Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5) 

        ttk.Label(mainFrame, text='Film:').grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        # Combobox
        self.txtFilm = StringVar()
        CbxFilm = ttk.Combobox(mainFrame, textvariable=self.txtFilm) 
        CbxFilm.grid(row=2, column=1, padx=5, pady=5) 

        # Add Combobox Film
        CbxFilm['value'] = ('Solo Leveling', 'Lampir', 'Aga Laen', 'Pasutri Gaje')
        CbxFilm.current()

        ttk.Label(mainFrame, text='Jadwal :').grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        # Combobox
        self.txtJadwal = StringVar() 
        CbxJadwal = ttk.Combobox(mainFrame, textvariable=self.txtJadwal)
        CbxJadwal.grid(row=3, column=1, padx=5, pady=5)

        # Add Combobox Jadwal
        CbxJadwal['values'] = ('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu')
        CbxJadwal.current()

        ttk.Label(mainFrame, text='Nomor Kursi:').grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        # Combobox Nomor Kursi
        self.txtNomorkursi = StringVar()
        CbxNomorkursi = ttk.Combobox(mainFrame,textvariable=self.txtNomorkursi) 
        CbxNomorkursi.grid(row=4, column=1, padx=5, pady=5)

        # Add Combobox
        CbxNomorkursi['value'] = ('A1','A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3')
        CbxNomorkursi.current()

        ttk.Label(mainFrame, text='Harga Tiket :').grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
        self.lbhHargaTiket = ttk.Label(mainFrame, text='') 
        self.lbhHargaTiket.grid(row=5, column=1, padx=5, pady=5)

        # Button
        self.btnSimpan = ttk.Button(mainFrame, text='Simpan', command=self.onSimpan, width= 10)
        self.btnSimpan.grid(row=6, column=0, padx=5, pady=5)
        self.btnClear = ttk.Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=6, column=1, padx=5, pady=5)
        self.btnHapus = ttk.Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=6, column=2, padx=5, pady=5)

        # define columns
        columns = ('id','no_transaksi', 'nama', 'film', 'jadwal', 'no_kursi', 'harga_tiket')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('no_transaksi', text='No Transaksi')
        self.tree.column('no_transaksi', width="80")
        self.tree.heading('nama', text='Nama')
        self.tree.column('nama', width="60")
        self.tree.heading('film', text='Film')
        self.tree.column('film', width="150")
        self.tree.heading('jadwal', text='Jadwal')
        self.tree.column('jadwal', width="100")
        self.tree.heading('no_kursi', text='Nomor Kursi')
        self.tree.column('no_kursi', width="80")
        self.tree.heading('harga_tiket', text='Harga Tiket')
        self.tree.column('harga_tiket', width="100")

        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()

        # Panggil updateHargaTiket() saat jadwal berubah
        CbxJadwal.bind("<<ComboboxSelected>>", self.updateHargaTiket)
    
    def updateHargaTiket(self, event=None):
        jadwal = self.txtJadwal.get()
        print('updae--->', jadwal)
        if jadwal in ['Sabtu','Minggu']:
            self.lbhHargaTiket.config(text="40000")
        
        else :
            self.lbhHargaTiket.config(text="30000")
        
    def onClear(self, event=None):
        self.txtNoTransaksi.delete(0, tk.END)
        self.txtNoTransaksi.insert(tk.END, "")
        self.txtNama.delete(0, tk.END)
        self.txtNama.insert(tk.END, "")       
        self.txtFilm.set('')
        self.txtJadwal.set('')
        self.txtNomorkursi.set('')
        self.lbhHargaTiket.config(text='') # Menghapus Text dari Label
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data bioskop
        b = Bioskop()
        result = b.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        subjects = []
        for row_data in result:
            subjects.append(row_data)

        for subject in subjects:
            self.tree.insert('', tk.END, values=subject)
    
    def onCari(self, event=None):
        no_transaksi = self.txtNoTransaksi.get()
        b = Bioskop()
        res = b.getByNoTransaksi(no_transaksi)
        rec = b.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtNoTransaksi.focus()
        return res
        
    def TampilkanData(self, event=None):
        no_transaksi = self.txtNoTransaksi.get()
        b = Bioskop()
        res = b.getByNoTransaksi(no_transaksi)
        self.txtNama.delete(0, tk.END)
        self.txtNama.insert(tk.END, b.nama)
        self.txtFilm.delete(0, tk.END)
        self.txtFilm.insert(tk.END, b.film)
        self.txtJadwal.delete(0, tk.END)
        self.txtJadwal.insert(tk.END, b.jadwal)   
        self.txtNomorkursi.delete(0, tk.END)
        self.txtNomorkursi.insert(tk.END, b.no_kursi)
        self.lbhHargaTiket.delete(0, tk.END)
        self.lbhHargaTiket.insert(tk.END, b.harga_tiket)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        no_transaksi = self.txtNoTransaksi.get()
        nama = self.txtNama.get()
        film = self.txtFilm.get()
        jadwal = self.txtJadwal.get()
        no_kursi = self.txtNomorkursi.get()
        harga_tiket = self.lbhHargaTiket.cget("text") # Ambil Text dari Label

        
        b = Bioskop()
        b.no_transaksi = no_transaksi
        b.nama = nama
        b.film = film
        b.jadwal = jadwal
        b.no_kursi = no_kursi
        b.harga_tiket = harga_tiket

        if self.ditemukan:
            res = b.updateByNoTransaksi(no_transaksi)
            ket = 'Diperbarui'
        else:
            res = b.simpan()
            ket = 'Disimpan'
            
        rec = b.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        no_transaksi = self.txtNoTransaksi.get()
        print('delete search ----->', self.ditemukan) # Tester Bugging 
        b = Bioskop()
        b.no_transaksi = no_transaksi
        if no_transaksi:
            res = b.deleteByNoTransaksi(no_transaksi)
            rec = b.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FrmBioskop(root, "Aplikasi Nonton Bioskop")
    root.mainloop()
