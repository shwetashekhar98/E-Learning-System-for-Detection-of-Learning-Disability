import os
from os import path
from pydub import AudioSegment
import speech_recognition as sr
import re
import tkinter
from tkinter import filedialog

import itertools
import difflib

def mp3_to_wav():
    filename1 =  filedialog.askopenfilename(initialdir = "C:/Users/Sri Satya Sai/Documents/BE Project/analysis/recordings/", title = "Select file",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
    print(filename1)

    dst = filedialog.asksaveasfilename(initialdir = "C:/Users/Sri Satya Sai/Documents/BE Project/analysis/recordings/", title = "Save As",filetypes = (("wav files","*.wav"),("all files","*.*")))
    print(dst)      

    sound = AudioSegment.from_mp3(filename1)
    sound.export(str(dst), format="wav")

def wav_text_up():
    filename2 =  filedialog.askopenfilename(initialdir = "C:/Users/Sri Satya Sai/Documents/BE Project/analysis/recordings/", title = "Select file",filetypes = (("wav files","*.wav"),("all files","*.*")))
    r = sr.Recognizer()
    file_audio = sr.AudioFile(filename2)
    with file_audio as source:
        r.adjust_for_ambient_noise(source,duration=0.5)
        audio = r.record(source)
        try:
            get = r.recognize_google(audio,language='en-IN')
        except  sr.UnknownValueError:
            print('error')
        except  sr.RequestError  as e:
            print('failed'.format(e))

    print(get.lower())
    obt = get.lower().split(" ")

    filename3 =  filedialog.askopenfilename(initialdir = "C:/Users/Sri Satya Sai/Documents/BE Project/analysis/corpus/", title = "Select file",filetypes = (("Text files","*.txt"),("all files","*.*")))
    f = open(filename3, 'r')
    orig = f.read().lower().split(" ")

    analysis(obt,orig)
    

def analysis(obt,orig):
    l = list(itertools.zip_longest(orig,obt))
    print(l)
    c,flag=0,0
    for i in range(len(l)):
        if l[i][0] != l[i][1]:
            if i!=len(l)-1:
                if l[i+1][0] != l[i][1]:
                    if i<len(l)-1-c-1:
                        if l[i+c+2][0] == l[i][1] and l[i+c+3][0] == l[i+1][1]:
                            #print(l[i+c][0])
                            #print(l[i+c+1][0])
                            c+=2

                    elif i==len(l)-1-c-1:
                        if l[i+c][0]!=l[i][1] and l[i+c+1][0]!=l[i][1]:
                            #print(l[i+c][0])
                            #print(l[i+c+1][0])
                            c+=2
            
            if i<len(l)-1-c:
                if l[i+c+1][0] == l[i][1]:
                    #print(l[i+c][0])
                    c+=1    

            elif i==len(l)-1-c:
                if flag==0:
                    if l[i+c][0]!=l[i][1]:
                        #print(l[i+c][0])
                        c+=1

    print("\nWords Omissions: %d"%c)        

    try:
        f = open('C:\\Users\\Sri Satya Sai\\Documents\\BE Project\\analysis\\corpus\\score.txt', 'r')
        v = f.read()
        f = open('C:\\Users\\Sri Satya Sai\\Documents\\BE Project\\analysis\\corpus\\score.txt', 'w')
        f.write(str(int(v)+c))
    except Exception:
        f = open('C:\\Users\\Sri Satya Sai\\Documents\\BE Project\\analysis\\corpus\\score.txt', 'w')
        f.write(str(c))
    f.close()

b1 = tkinter.Button(text='Click to Convert file from mp3 to wav format', command=mp3_to_wav).pack()
b2 = tkinter.Button(text='Click to upload wav and text file', command=wav_text_up).pack()
tkinter.mainloop()