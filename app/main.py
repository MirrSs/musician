from pydub import AudioSegment
from pydub.playback import play

# song = AudioSegment.from_mp3("/home/mirrss/work/musician/music/nirvana.mp3")
# play(song)

from tkinter import *
from tkinter import filedialog

def add_song():
    files = filedialog.askopenfilenames()
    for file in files:
        song = AudioSegment.from_mp3("/home/mirrss/work/musician/music/nirvana.mp3")
        play(song)

window = Tk()

btn = Button(window, text="Add song",command=add_song)
btn.grid(column=1, row=0)

window.title("Musician")
window.mainloop()
