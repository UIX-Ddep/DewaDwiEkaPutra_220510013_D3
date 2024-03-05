from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W, font

class FrmDosen:
    
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        label = Label(mainFrame, text="Dosen Content", font=font.Font(size=40))
        label.pack(padx=20, pady=20)
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi 
        self.parent.destroy()
      
if __name__ == '__main__':
    def update_main_window(result):
        print(result)

    root = Tk()
    aplikasi = FrmDosen(root, "Windows Dosen")
    root.mainloop()