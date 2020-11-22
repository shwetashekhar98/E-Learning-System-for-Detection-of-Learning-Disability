import os
from os import path
from pydub import AudioSegment
import speech_recognition as sr
import re
from tkinter import filedialog
from tkinter import *
import tkinter
def mp3_to_wav():
    filename1 =  filedialog.askopenfilename(initialdir = "C:/Users/Shweta/Documents/Sound recordings", title = "Select file",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
    #print(filename1)
    dst = filedialog.asksaveasfilename(initialdir = "C:/Users/Shweta/Documents/Sound recordings", title = "Save As",filetypes = (("wav files","*.wav"),("all files","*.*")))
    #print(dst)  
    sound = AudioSegment.from_mp3(filename1)
    sound.export(str(dst), format="wav")


def wav_text_up():
    r = sr.Recognizer()
    filename2 =  filedialog.askopenfilename(initialdir = "C:/Users/Shweta/Documents/Sound recordings", title = "Select file",filetypes = (("wav files","*.wav"),("all files","*.*")))
    file_audio = sr.AudioFile(filename2)
    with file_audio as source:
        audio = r.record(source)
        try:
            get = r.recognize_google(audio)
        except  sr.UnknownValueError:
            print('error')
        except  sr.RequestError  as e:
            print('failed'.format(e))
    print(get)
    line_number = 0
    list_of_results = []
    #string=input("Enter the string")
    filename3 =  filedialog.askopenfilename(initialdir = "C:/Users/Shweta/Desktop", title = "Select file",filetypes = (("Text files","*.txt"),("all files","*.*")))
    with open(filename3, 'r') as read_obj:
        for line in read_obj:
            line_number += 1
            if get in line:
                list_of_results.append((line_number, line.rstrip()))

        if(len(list_of_results)==0):
            print("Accuracy is 0%")
        else:
            for elem in list_of_results:
                print('Line Number = ', elem[0], ' :: Line with accuracy = ', elem[1])
b1 = tkinter.Button(text='Click to Convert file from mp3 to wav format', command=mp3_to_wav).pack()
b2 = tkinter.Button(text='Click to upload wav and text file', command=wav_text_up).pack()
tkinter.mainloop() 

