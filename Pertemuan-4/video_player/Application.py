
import sys
import platform
import os

from PyQt5 import QtCore,QtWidgets,QtGui


import vlc
import time as STimmer

class Application(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.setWindowTitle("Media Player")
        #create a simple Instance
        self.Vlc_Instance=vlc.Instance()
        
        self.Media=None

        #creating empty vlc media Player
        self.MPlayer=self.Vlc_Instance.media_player_new()
        

        #Initalize the user interface 
        self.Init_GUI()
        #Pause var for check if song is in pause mode or not !
        self.Is_pasue=False
        self.Is_Vframe_Hidden=False
        self.IS_Audio_File=False

        
        """
        # Timmer vars
        using Timmer to calcualting the elapse time while playing the song !
        """
        self._second=0
        self._minutes=0
        self._hour=0


    def Init_GUI(self):
        print(platform.system())
        """
        Creating a Centeral Widget That's Hold The child widgets such as button ,slider etc..
        """
        self.widget=QtWidgets.QWidget(self)
        #set it as centeral widget element
        self.setCentralWidget(self.widget)
        #self.widget.setToolTip("hai")

        #Creating Vedio Frame element whichs shows the each frame of the vedio
        # In this widget, the video will be drawn
        if platform.system() == "Darwin": # for MacOS
            self.VideoFrame = QtWidgets.QMacCocoaViewContainer(0)
        else:
            self.VideoFrame = QtWidgets.QFrame()
            

        #just for QFrame to customize [setting the color ]
        self.Pallet=self.VideoFrame.palette()
        self.Pallet.setColor(QtGui.QPalette.Window,QtGui.QColor(0, 9, 0))
        self.VideoFrame.setPalette(self.Pallet)
        self.VideoFrame.setAutoFillBackground(True)
        
        #Slider Setup
        self.MSlider=QtWidgets.QSlider(QtCore.Qt.Horizontal,self)
        self.MSlider.setMaximum(1000)
        #need to add slider postion update fun
        self.MSlider.sliderMoved.connect(self.set_position)
        self.MSlider.sliderPressed.connect(self.set_position)
        

        #Play Button
        self.Hbox=QtWidgets.QHBoxLayout()
        self.Playbutton=QtWidgets.QPushButton("Play")
        self.Hbox.addWidget(self.Playbutton)
        self.Playbutton.clicked.connect(self.play_pause)
       
        #self.widget.setLayout(self.Hbox)
        
        #stop Button
        self.Stopbutton=QtWidgets.QPushButton("Stop")
        self.Hbox.addWidget(self.Stopbutton)
        self.Stopbutton.clicked.connect(self.Stop)
        self.Hbox.addStretch(1)
        self.Time_duration=QtWidgets.QLabel("0:0:0")
        self.Hbox.addWidget(self.Time_duration)
        #Volume Slider
        self.Hbox.addStretch(1)
        self.VolumeSlider=QtWidgets.QSlider(QtCore.Qt.Horizontal,self)
        self.VolumeSlider.setMaximum(100)
        self.VolumeSlider.setValue(self.MPlayer.audio_get_volume())
        self.Hbox.addWidget(self.VolumeSlider)
        self.VolumeSlider.valueChanged.connect(self.set_Volume)

        #setting the vertical Layout
        self.Vbox_Layout=QtWidgets.QVBoxLayout()
        self.Vbox_Layout.addWidget(self.VideoFrame)
        self.Vbox_Layout.addWidget(self.MSlider)
        self.Vbox_Layout.addLayout(self.Hbox)



        self.widget.setLayout(self.Vbox_Layout)
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu("File")

        # Add actions to file menu
        open_action = QtWidgets.QAction("Load File", self)
        close_action = QtWidgets.QAction("Close App", self)
        file_menu.addAction(open_action)
        file_menu.addAction(close_action)

        open_action.triggered.connect(self.open_file)
        close_action.triggered.connect(sys.exit)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(100)
        self.time=QtCore.QTime(0,0,0)
        self.timer.timeout.connect(self.timerEvent)
        self.timer.timeout.connect(self.update_ui)

    #Play and pause method where media can pause and resume 
    def play_pause(self):
        """Toggle play/pause status
        """
        if self.MPlayer.is_playing():
            self.MPlayer.pause()
            self.Playbutton.setText("Play")
            self.is_paused = True
            self.timer.stop()
        else:
            if self.MPlayer.play() == -1:
                self.open_file()
                return
               
            #check if vedio frame is hidden 
            if self.IS_Audio_File:
                self.VideoFrame.hide()
                self.Is_Vframe_Hidden=True
                self.resize(500,100)

            self.MPlayer.play()
            self.Playbutton.setText("Pause")
            self.timer.start()
            self.is_paused = False
    #Stop Media Player
    def Stop(self):
        """
            Stop player
        """
        self.MPlayer.stop()
        self.Playbutton.setText("Play")
        self.timer.stop()
        self.timer.setInterval(100)
        if self.Is_Vframe_Hidden:
            self.VideoFrame.show()
            self.Is_Vframe_Hidden=False
            self.resize(640,480)
    
    def open_file(self):
        """
            Open a media file in a MPlayer
        """

        dialog_txt = "Choose Media File"
        filename = QtWidgets.QFileDialog.getOpenFileName(self, dialog_txt, os.path.expanduser('~'))
        #check if anything got if not empty just pass else return 
        if filename[0]!= "":
            #before returning if it's an audio file resize the media player
            self.filename,self.file_extension=os.path.splitext(filename[0])
            print(self.file_extension)
            if self.file_extension == ".mp3" or self.file_extension == ".wav":
                self.VideoFrame.hide()
                self.resize(500,100)
                self.Is_Vframe_Hidden=True
                self.IS_Audio_File=True
            else:
                self.VideoFrame.show()
                self.resize(640,480)
                self.IS_Audio_File=False
                pass
        else:
            return 


        # getOpenFileName returns a tuple, so use only the actual file name
        self.media = self.Vlc_Instance.media_new(filename[0])

        # Put the media in the media player
        self.MPlayer.set_media(self.media)

        # Parse the metadata of the file
        self.media.parse()

        # Set the title of the track as window title
        self.setWindowTitle(self.media.get_meta(0))

        # The media player has to be 'connected' to the QFrame (otherwise the
        # video would be displayed in it's own window). This is platform
        # specific, so we must give the ID of the QFrame (or similar object) to
        # vlc. Different platforms have different functions for this
        if platform.system() == "Linux": # for Linux using the X Server
            self.MPlayer.set_xwindow(int(self.VideoFrame.winId()))
        elif platform.system() == "Windows": # for Windows
            self.MPlayer.set_hwnd(int(self.VideoFrame.winId()))
        elif platform.system() == "Darwin": # for MacOS
            self.MPlayer.set_nsobject(int(self.VideoFrame.winId()))

        self.play_pause()

    def update_ui(self):
        """Updates the user interface"""

        # Set the slider's position to its corresponding media position
        # Note that the setValue function only takes values of type int,
        # so we must first convert the corresponding media position.
        media_pos = int(self.MPlayer.get_position() * 1000)
        self.MSlider.setValue(media_pos)

        # No need to call this function if nothing is played
        if not self.MPlayer.is_playing():
            self.timer.stop()

            # After the video finished, the play button stills shows "Pause",
            # which is not the desired behavior of a media player.
            # This fixes that "bug".
            if not self.is_paused:
                self.Stop()
    

    def set_position(self):
        """Set the movie position according to the position slider.
        """

        # The vlc MPlayer needs a float value between 0 and 1, Qt uses
        # integer variables, so you need a factor; the higher the factor, the
        # more precise are the results (1000 should suffice).

        # Set the media position to where the slider was dragged
        self.timer.stop()
        pos = self.MSlider.value()
        self.MPlayer.set_position(pos / 1000.0)
        self.timer.start()
    
    def set_Volume(self, volume):
        """Set the volume
        """
        self.MPlayer.audio_set_volume(volume)
        #self.data=vlc.Media.parse(self.Vlc_Instance)
        self.length=self.MPlayer.get_length()/1000
        self.mm,self.ss=divmod(self.length,60)
        print("mm",round(self.mm,0),"ss",round(self.ss,0))
        #print(self.timer.)

    def timerEvent(self):
        #self.time=self.time.addSecs(1)
        media_pos = int(self.MPlayer.get_position() * 1000)
        STimmer.sleep(1)
        print(self._hour,":",self._minutes,":",self._second)
        self._second+=1
        if (self._second==60):
            self._second=0
            self._minutes+=1
        if (self._minutes==60):
            self._minutes=0
            self._hour+=1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    player = Application()
    player.show()
    player.resize(640,480)
    sys.exit(app.exec_())