import tkinter as tk
from tkinter import Menu, messagebox
from FrmLogin import *
from FrmBioskop import *

class Dashboard:
    def __init__(self):
        # root window
        self.root = tk.Tk()
        self.root.title('Menu Demo')
        # self.root.attributes('-fullscreen', True)
        self.root.geometry("900x400")
        self.__data = None
        self.__level = None
        # create a menubar
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        # create menus
        self.file_menu = Menu(self.menubar)
        self.admin_menu = Menu(self.menubar)

        # add menu items to File menu
        self.file_menu.add_command(label='Login', command=lambda: self.new_window("Log Me In", FrmLogin))
        self.file_menu.add_command(label='Exit', command=self.root.destroy)

        # add menu items to menu Bioskop
        self.admin_menu.add_command(label='Bioskop', command=lambda: self.new_window("Bioskop", FrmBioskop))

        # add menus to the menubar
        self.menubar.add_cascade(label="File", menu=self.file_menu)

    def new_window(self, number, _class, update_main_window=None):
        new = tk.Toplevel(self.root)
        new.transient()
        new.grab_set()
        # if update_main_window:
        #     _class(new, number, update_main_window)
        # else:
        _class(new, number, self.update_main_window)

    def update_main_window(self, data):
        # Method to receive data from child windows
        self.__data = data
        level = self.__data[0]
        loginvalid = self.__data[1]
        if(loginvalid==True):
            index = self.file_menu.index('Login')
            # hapus menu login
            self.file_menu.delete(index)
            self.file_menu.add_command(label='Bioskop', command=lambda: self.new_window("Bioskop", FrmBioskop))
            self.file_menu.add_command(label='Logout', command=self.Logout)
        

    def Logout(self):
        index = self.file_menu.index('Logout')
        self.file_menu.delete(index)
        self.file_menu.add_command(label='Login', command=lambda: self.new_window("Log Me In", FrmLogin, self.update_main_window))
        self.remove_all_menus()

    def remove_all_menus(self):
        index = self.menubar.index(self.__level)
        if index is not None:
            self.menubar.delete(index)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    menu_app = Dashboard()
    menu_app.run()
