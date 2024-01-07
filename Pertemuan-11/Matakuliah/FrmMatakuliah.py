import tkinter as tk
from tkinter import ttk, messagebox
from Matakuliah import Matakuliah

class FormMatakuliah:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = ttk.Frame(self.parent, borderwidth=10)  # Use 'borderwidth' instead of 'bd'
        mainFrame.pack(fill=tk.BOTH, expand=tk.YES)
        
        # Label
        ttk.Label(mainFrame, text='Kode MK:').grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtKodeMK = ttk.Entry(mainFrame) 
        self.txtKodeMK.grid(row=0, column=1, padx=5, pady=5) 
        self.txtKodeMK.bind("<Return>", self.onCari)

        ttk.Label(mainFrame, text='Nama MK:').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtNamaMK = ttk.Entry(mainFrame) 
        self.txtNamaMK.grid(row=1, column=1, padx=5, pady=5) 

        ttk.Label(mainFrame, text='SKS:').grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtSKS = ttk.Entry(mainFrame) 
        self.txtSKS.grid(row=2, column=1, padx=5, pady=5) 

        # Button
        self.btnSimpan = ttk.Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = ttk.Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = ttk.Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('id', 'kodemk', 'namamk', 'sks')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('kodemk', text='Kode MK')
        self.tree.column('kodemk', width="60")
        self.tree.heading('namamk', text='Nama MK')
        self.tree.column('namamk', width="200")
        self.tree.heading('sks', text='SKS')
        self.tree.column('sks', width="30")
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtKodeMK.delete(0, tk.END)
        self.txtKodeMK.insert(tk.END, "")
        self.txtNamaMK.delete(0, tk.END)
        self.txtNamaMK.insert(tk.END, "")       
        self.txtSKS.delete(0, tk.END)
        self.txtSKS.insert(tk.END, "")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data matakuliah
        mk = Matakuliah()
        result = mk.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        subjects = []
        for row_data in result:
            subjects.append(row_data)

        for subject in subjects:
            self.tree.insert('', tk.END, values=subject)
    
    def onCari(self, event=None):
        kodemk = self.txtKodeMK.get()
        mk = Matakuliah()
        res = mk.getByKodeMk(kodemk)
        rec = mk.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtNamaMK.focus()
        return res
        
    def TampilkanData(self, event=None):
        kodemk = self.txtKodeMK.get()
        mk = Matakuliah()
        res = mk.getByKodeMk(kodemk)
        self.txtNamaMK.delete(0, tk.END)
        self.txtNamaMK.insert(tk.END, mk.namamk)
        self.txtSKS.delete(0, tk.END)
        self.txtSKS.insert(tk.END, mk.sks)   
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        kodemk = self.txtKodeMK.get()
        namamk = self.txtNamaMK.get()
        sks = self.txtSKS.get()
        
        mk = Matakuliah()
        mk.kodemk = kodemk
        mk.namamk = namamk
        mk.sks = sks
        if self.ditemukan:
            res = mk.updateByKodeMk(kodemk)
            ket = 'Diperbarui'
        else:
            res = mk.simpan()
            ket = 'Disimpan'
            
        rec = mk.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        kodemk = self.txtKodeMK.get()
        mk = Matakuliah()
        mk.kodemk = kodemk
        if self.ditemukan:
            res = mk.deleteByKodeMk(kodemk)
            rec = mk.affected
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
    aplikasi = FormMatakuliah(root, "Aplikasi Data Matakuliah")
    root.mainloop()
