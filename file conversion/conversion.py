import os
from os import path
from pydub import AudioSegment
from tkinter import filedialog
import tkinter
def m4a_to_mp3():
    filename1 =  filedialog.askopenfilename(initialdir = "C:/Users/Shweta/Documents/Sound recordings", title = "Select file",filetypes = (("m4a files","*.m4a"),("all files","*.*")))
    #print(filename1)
    m4a_audio = AudioSegment.from_file(filename1, format="m4a")
    dst = filedialog.asksaveasfilename(initialdir = "C:/Users/Shweta/Documents/Sound recordings", title = "Save As",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
    print(dst)
    m4a_audio.export(str(dst), format="mp3")

def mp3_to_wav():
    dst1 = filedialog.askopenfilename(initialdir = "C:/Users/Shweta/Documents/Sound recordings", title = "Select file",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
    print(dst1)                                                      
    sound = AudioSegment.from_mp3(dst1)
    dst2 = filedialog.asksaveasfilename(initialdir = "C:/Users/Shweta/Documents/Sound recordings", title = "Save As",filetypes = (("wav files","*.wav"),("all files","*.*")))
    print(dst2)
    sound.export(str(dst2), format="wav")


    
b1 = tkinter.Button(text='Convert m4a to mp3', command=m4a_to_mp3).pack()
b2 = tkinter.Button(text='Convert mp3 to wav', command=mp3_to_wav).pack()
tkinter.mainloop() 

