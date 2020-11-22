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
    over_count=0
    print(l)
    def reversal(s1,s2):
        count=0
        for x,y in zip(s1,s2):
            if x=='b' and y=='d':
                count+=1
            if x=='d' and y=='b':
                count+=1
            if x=='m' and y=='w':
                count+=1
            if x=='w' and y=='m':
                count+=1
            if x=='n' and y=='u':
                count+=1
            if x=='u' and y=='n':
                count+=1
            if x=='p' and y=='q':
                count+=1
            if x=='q' and y=='p':
                count+=1
        return count

    ch = input("\nEnter s - substitution, r - reversal, m - mispronunciation, ps - prefix/suffix OR Enter 'e' to exit: ")
    while ch!='e':
        if ch == 's':
            #print(l)
            c=0
            for i in range(len(l)):
                if l[i][0] != l[i][1]:
                    if i!=len(l)-1:
                        if l[i+1][0] != l[i+1][1]:
                            if i+1==len(l)-1:
                                #print(l[i][0],l[i][1])
                                #print(l[i+1][0],l[i+1][1])
                                c+=2
                            elif i==0:
                                #print(l[i][0],l[i][1])
                                #print(l[i+1][0],l[i+1][1])
                                c+=2
                            else:
                                if l[i-1][0] == l[i-1][1] and l[i+2][0] == l[i+2][1]:
                                    #print(l[i][0],l[i][1])
                                    #print(l[i+1][0],l[i+1][1])
                                    c+=2
                        else:    
                            if i==0:
                                if l[i+1][0] == l[i+1][1]:
                                    #print(l[i][0],l[i][1])
                                    c+=1
                            else:
                                if l[i-1][0] == l[i-1][1] and l[i+1][0] == l[i+1][1]:
                                    #print(l[i][0],l[i][1])
                                    c+=1
                    else:    
                        if l[i-1][0] == l[i-1][1]:
                            #print(l[i][0],l[i][1])
                            c+=1

            print("\nWords Substitutions: %d"%c)
            over_count+=c

        if ch == 'r':
            #print(l)
            c=0
            for i in range(len(l)):
                if l[i][0] != l[i][1]:
                    if reversal(l[i][0],l[i][1])>0:
                        #print(l[i][0],l[i][1],reversal(l[i][0],l[i][1]))
                        c+=1

            print("\nWords Reversals: %d"%c)
            over_count+=c

        if ch == 'm':
            c=0
            words,corig,cobt,diff=[],[],[],[]
            for w in orig:
                if w not in words:
                    words.append(w)
            for _ in range(len(words)):
                corig.append(0)
                cobt.append(0)    
            for z in range(len(words)):
                for x,y in zip(orig,obt):
                    if words[z]==x:
                        corig[z]+=1
                    if words[z]==y:
                        cobt[z]+=1
                        
            for x,y,z in zip(words,corig,cobt):
                if z/y < 0.3:
                    #print("Word: %s, Original Occurence: %d, Obtained Occurence: %d"%(x,y,z))
                    c+=1

            print("\nWords Mispronuniations: %d"%c)
            over_count+=c

        if ch == 'ps':
            c=0
            for a,b in l: 
                if a in b:
                    suf,pre=[],[]
                    pfx=['en','in','un','re','dis']
                    sfx=['y','ly','ing','d','ed','er','al','es','ion','s']
                    pos=0  
                    for i,s in enumerate(difflib.ndiff(a, b)):
                        if s[0]==' ': continue
                        elif s[0]=='+':
                            if i==0 or i==pos+1:
                                pre.append(s[-1])
                                pos=i
                            else:
                                suf.append(s[-1])
                    prefix = "".join(pre)
                    suffix = "".join(suf)
                    if prefix in pfx or suffix in sfx:
                        '''print('{} => {}'.format(a,b))
                        if prefix in pfx:
                            print("Prefix: "+prefix)
                        if suffix in sfx:
                            print("Suffix: "+suffix)'''
                        c+=1

            print("\nWords Prefix/Suffix Additions: %d"%c)
            over_count+=c

            try:
                f = open('C:\\Users\\Sri Satya Sai\\Documents\\BE Project\\analysis\\corpus\\score.txt', 'r')
                v = f.read()
                over_count=over_count+int(v)
                f = open('C:\\Users\\Sri Satya Sai\\Documents\\BE Project\\analysis\\corpus\\score.txt', 'w')
                f.write(str(over_count))
            except Exception:
                f = open('C:\\Users\\Sri Satya Sai\\Documents\\BE Project\\analysis\\corpus\\score.txt', 'w')
                f.write(str(over_count))
            f.close()
            
            print("\nTotal Errors: %d"%over_count)
            if over_count/len(orig)>0.3:
                print("\nHaving Miscue Problem")
            else:
                print("\nNot Having Miscue Problem")
            
        ch = input("\nEnter s - substitution, r - reversal, m - mispronunciation, ps - prefix/suffix OR Enter 'e' to exit: ")

b1 = tkinter.Button(text='Click to Convert file from mp3 to wav format', command=mp3_to_wav).pack()
b2 = tkinter.Button(text='Click to upload wav and text file', command=wav_text_up).pack()
tkinter.mainloop()