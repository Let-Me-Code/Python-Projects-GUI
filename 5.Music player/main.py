import os
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer

root = Tk()

# Create the menuBar
menuBar = Menu(root)
root.config(menu=menuBar)

# Create submenu
subMenu = Menu(menuBar, tearoff=0)  # tearoff no dash line


def browse_file():
    global filename
    filename = filedialog.askopenfilename()


menuBar.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='Open', command=browse_file)
subMenu.add_command(label='Exit', command=root.destroy)


def about_us():
    tkinter.messagebox.showinfo('About BMX Player', 'This is the a music player using Python tkinter')


subMenu = Menu(menuBar, tearoff=0)  # tearoff no dash line
menuBar.add_cascade(label='Help', menu=subMenu)
menuBar.add_command(label='About us', command=about_us)

mixer.init()  # initializing the mixer

# root.geometry('300x300')
root.title('BMX Player')
root.iconbitmap('images/melody.ico')

text = Label(root, text="Relax your Soul!")
text.pack(pady=10)


class Player:

    def play_music(self):
        try:
            paused  # checking paused initialized or not
        except NameError:
            try:
                mixer.music.load(filename)  # name of the song
                mixer.music.play()
                statusbar['text'] = 'Playing music' + '-' + os.path.basename(filename)
            except:
                tkinter.messagebox.showerror('File not found', 'Melody is not found music')
                print('Error')
        else:
            mixer.music.unpause()
            statusbar['text'] = 'Music Resumed'

    def pause_music(self):
        global paused
        paused = TRUE
        mixer.music.pause()
        statusbar['text'] = 'Music paused'


player_x = Player()


middleFrame = Frame(root)  # relief=RAISED, borderwidth=1
middleFrame.pack(pady=10)


playphoto = PhotoImage(file='images/play.png')
playBtn = Button(middleFrame, image=playphoto, command=player_x.play_music)
playBtn.grid(row=0, column=0, padx=10)


pausePhoto = PhotoImage(file='images/pause.png')
pauseBtn = Button(middleFrame, image=pausePhoto, command=player_x.pause_music)
pauseBtn.grid(row=0, column=1, padx=10)


def stop_music():
    mixer.music.stop()
    statusbar['text'] = 'Music stopped'


stopPhoto = PhotoImage(file='images/stop.png')
stopBtn = Button(middleFrame, image=stopPhoto, command=stop_music)
stopBtn.grid(row=0, column=2, padx=10)


def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)  # set_value takes value from 0 to 1


scale = Scale(root, from_=0, to=100,
              orient=HORIZONTAL,
              command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.pack(pady=15)

statusbar = Label(root, text='Welcome to BMX Player',
                  relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
