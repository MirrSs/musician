from glob import glob
from tkinter import *
from tkinter import filedialog

import pygame

playlist = []

def add_song():
    file_list:tuple = filedialog.askopenfilenames(initialdir='music',title='Choose a song',filetypes=(('mp3 Files','*.mp3'),('wav Files','*.wav')))
    songs = []
    for file in file_list:
        playlist.append(file)
        temp_song = file.rsplit('/')[-1]
        temp_song = temp_song.rsplit('.')[0]
        songs.append(temp_song)
    for song in songs:   
        playlist_box.insert(END, song)

def play_song():
    song = playlist_box.get(ACTIVE)
    for file in playlist:
        if file.find(song)>=0:
            pygame.mixer.music.load(file)
            pygame.mixer.music.play(loops=0)

#Pause and Unpause the current song
global paused
paused = False
def pause_song(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def stop_song():
     pygame.mixer.music.stop()
     playlist_box.select_clear(ACTIVE)

def delete_song_from_playlist():
    song = playlist_box.selection_get()
    for file in playlist:
        if file.find(song)>=0:
            playlist.remove(file)
    song = playlist_box.curselection()
    playlist_box.delete(song)

def next_song():
    current_song = playlist_box.curselection()
    song = playlist_box.get(current_song[0]+1)
    for file in playlist:
        if file.find(song)>=0:
            pygame.mixer.music.load(file)
            pygame.mixer.music.play(loops=0)
    
    #move active bar in playlist
    playlist_box.selection_clear(0,END)
    playlist_box.activate(current_song[0]+1)
    playlist_box.selection_set(current_song[0]+1,last=None)

def prev_song():
    current_song = playlist_box.curselection()
    song = playlist_box.get(current_song[0]-1)
    for file in playlist:
        if file.find(song)>=0:
            pygame.mixer.music.load(file)
            pygame.mixer.music.play(loops=0)
    
    #move active bar in playlist
    playlist_box.selection_clear(0,END)
    playlist_box.activate(current_song[0]-1)
    playlist_box.selection_set(current_song[0]-1,last=None)


window = Tk()

window.geometry('550x350')

#mixer init
pygame.mixer.init()

#Create playlist box
playlist_box = Listbox(window,bg='black',fg='white',width=60)
playlist_box.pack(pady=20)

controls_frame = Frame(window)
controls_frame.pack()

#Button images
backward_btn_img = PhotoImage(file='images/backward.png')
forward_btn_img = PhotoImage(file='images/forward.png')
play_btn_img = PhotoImage(file='images/play.png')
stop_btn_img = PhotoImage(file='images/stop.png')
pause_btn_img = PhotoImage(file='images/pause.png')
add_btn_img = PhotoImage(file='images/add_song.png')
delete_btn_img = PhotoImage(file='images/trash1.png')

backward_btn = Button(controls_frame,image=backward_btn_img,borderwidth=0,command=prev_song)
forward_btn = Button(controls_frame,image=forward_btn_img,borderwidth=0,command=next_song)
play_btn = Button(controls_frame,image=play_btn_img,borderwidth=0,command=play_song)
pause_btn = Button(controls_frame,image=pause_btn_img,borderwidth=0,command=lambda: pause_song(paused))
stop_btn = Button(controls_frame,image=stop_btn_img,borderwidth=0,command=stop_song)
add_btn = Button(controls_frame,image=add_btn_img,borderwidth=0,command=add_song)
delete_btn = Button(controls_frame,image=delete_btn_img,borderwidth=0,command=delete_song_from_playlist)

backward_btn.grid(row=0,column=0,padx=7)
forward_btn.grid(row=0,column=1,padx=7)
play_btn.grid(row=0,column=2,padx=7)
pause_btn.grid(row=0,column=3,padx=7)
stop_btn.grid(row=0,column=4,padx=7)
add_btn.grid(row=0,column=5,padx=7)
delete_btn.grid(row=0,column=6,padx=7)

window.title("Musician")
window.mainloop()
