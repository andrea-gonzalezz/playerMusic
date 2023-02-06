import tkinter as tk
import os
import fnmatch
from tkinter import *
from pygame import mixer

window = tk.Tk()
window.title('Python Music Player')
window.geometry("500x500")
window.config(bg="black")
window.resizable(False, False)


#chemin où se trouvent les musiques
rootpath = "C://Users/andre/Desktop/player-music2/music"
pattern = "*.mp3"

mixer.init()

#Images boutons
prec = PhotoImage(file = "next-button.png")
stop = PhotoImage(file = "stop-button.png")
play = PhotoImage(file = "play-button.png")
pause = PhotoImage(file = "pause-button.png")
suivant = PhotoImage(file = "next-button.png")

def select_play():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath +"//" + listBox.get("anchor"))
    mixer.music.play()

def select_stop():
    mixer.music.stop()
    listBox.select_clear('active')

def select_suivant():
    next_song = listBox.curselection()
    next_song =next_song[0]+1
    next_song_name= listBox.get(next_song)

    label.config(text=next_song_name)
    mixer.music.load(rootpath + "//" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def select_prec():
    prec_song = listBox.curselection()
    prec_song =prec_song[0]-1
    prec_song_name= listBox.get(prec_song)

    label.config(text=prec_song_name)
    mixer.music.load(rootpath + "//" + prec_song_name)
    mixer.music.play()

    listBox.select_clear(0,'end')
    listBox.activate(prec_song)
    listBox.select_set(prec_song)

def select_pause():
    mixer.music.pause()

#Cadre où s'afficheront les musiques
listBox=tk.Listbox(window, fg="white", bg="grey", width= 100, font=("Arial",14))
listBox.pack(padx =15, pady=15)


label=tk.Label(window, text="", bg='black')
label.pack(padx=15, pady=15)

top = tk.Frame(window, bg="black")
top.pack(padx=10, pady=5, anchor='center')


#Creation des boutons

precButton = tk.Button(window, image=prec, bg='black', width=60, height=60, bd=0, command= select_prec)
precButton.pack(pady=15, in_=top, side=LEFT)
stopButton = tk.Button(window, image=stop, bg='black', width=60, height=60, bd=0, command=select_stop)
stopButton.pack(pady=15, in_=top, side=LEFT)
playButton = tk.Button(window, image=play, bg='black', width=60, height=60, bd=0, command=select_play)
playButton.pack(pady=15, in_=top, side=LEFT)
pauseButton = tk.Button(window, image=pause, bg='black', width=60, height=60, bd=0, command = select_pause)
pauseButton.pack(pady=15, in_=top, side=LEFT)
nextButton = tk.Button(window, image=suivant, bg='black', width=60, height=60, bd=0, command=select_suivant)
nextButton.pack(pady=15, in_=top, side=LEFT)



for root, dirs, files, in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listBox.insert('end', filename)




window.mainloop()