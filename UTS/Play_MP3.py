import os
import pygame
from tkinter import Tk, Button, Label, filedialog, Scale

class MP3Player:
    def __init__(self, master):
        self.master = master
        self.master.title("MP3 Player")
        self.master.geometry("400x200")
        self.master.resizable(False,False)

        self.current_file = None
        self.playing = False

        # Set up a simple blue and white color scheme
        self.master.configure(bg="#AFC8AD")
        self.label_color = "#ffffff"
        self.button_color = "#9EC8B9"

        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self.master, text="Insert file selected", bg="#3498db", fg=self.label_color)
        self.label.pack(pady=10)

        self.select_button = Button(self.master, text="Select MP3", command=self.select_file, bg=self.button_color, fg=self.label_color)
        self.select_button.pack(pady=5)

        self.play_button = Button(self.master, text="Play", command=self.play_pause, bg=self.button_color, fg=self.label_color)
        self.play_button.pack(pady=5)

        self.stop_button = Button(self.master, text="Stop", command=self.stop_music, bg=self.button_color, fg=self.label_color)
        self.stop_button.pack(pady=5)

        self.volume_label = Label(self.master, text="Volume:", bg="#3498db", fg=self.label_color)
        self.volume_label.pack(pady=5)

        self.volume_slider = Scale(self.master, from_=0, to=100, orient="horizontal", command=self.set_volume, bg="#3498db", fg=self.label_color)
        self.volume_slider.set(70)  # Initial volume level
        self.volume_slider.pack(pady=5)

    def select_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])

        if file_path:
            self.current_file = file_path
            self.label.config(text=os.path.basename(file_path))

    def play_pause(self):
        if not self.current_file:
            return

        if not self.playing:
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(self.current_file)
            pygame.mixer.music.set_volume(self.volume_slider.get() / 100.0)
            pygame.mixer.music.play()
            self.playing = True
            self.play_button.config(text="Pause")
        else:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
                self.playing = False
                self.play_button.config(text="Play")

    def stop_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            self.playing = False
            self.play_button.config(text="Play")

    def set_volume(self, val):
        if self.playing:
            pygame.mixer.music.set_volume(float(val) / 100.0)

if __name__ == "__main__":
    root = Tk()
    mp3_player = MP3Player(root)
    root.mainloop()
