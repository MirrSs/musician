from tkinter import *
from tkinter import filedialog

import pygame

window = Tk()

window.geometry('500x300')

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

backward_btn = Button(controls_frame,image=backward_btn_img,borderwidth=0)
forward_btn = Button(controls_frame,image=forward_btn_img,borderwidth=0)
play_btn = Button(controls_frame,image=play_btn_img,borderwidth=0)
pause_btn = Button(controls_frame,image=pause_btn_img,borderwidth=0)
stop_btn = Button(controls_frame,image=stop_btn_img,borderwidth=0)

backward_btn.grid(row=0,column=0,padx=7)
forward_btn.grid(row=0,column=1,padx=7)
play_btn.grid(row=0,column=2,padx=7)
pause_btn.grid(row=0,column=3,padx=7)
stop_btn.grid(row=0,column=4,padx=7)


#window.iconphoto('images/desktop.png')
window.title("Musician")
window.mainloop()
