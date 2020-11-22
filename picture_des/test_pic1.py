import os
from os import path
from pydub import AudioSegment
import speech_recognition as sr
import re
from tkinter import filedialog
from tkinter import *
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
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
    
  
    #X = input("Enter first string: ").lower() 
    # Y = input("Enter second string: ").lower() 
    
    
    # tokenization 
    X_list = word_tokenize(get.lower())  
    
  
    # sw contains the list of stopwords 
    sw = stopwords.words('english')  
      
    # remove stop words from string 
    X_set = {w for w in X_list if not w in sw}
    print(X_set)
  
    #line_number = 0
    #list_of_results = []
    #list1=[]
    #string=get.lower()
    list1=[]
    filename3 =  filedialog.askopenfilename(initialdir = "C:/Users/Shweta/Desktop", title = "Select file",filetypes = (("Text files","*.txt"),("all files","*.*")))
    #f = open(filename3, 'r')
    with open(filename3, 'r') as read_obj:
        for line in read_obj:
            Y_list = word_tokenize(line.lower()) 
            #print(Y_list)
            #list1.extend(Y_list)
            #print(list1)
            Y_set = {w for w in Y_list if not w in sw}
            #print(Y_set)   
            

            l1=[];l2=[]
            # form a set containing keywords of both strings  
            rvector = X_set.union(Y_set)  
            for w in rvector: 
                if w in X_set: l1.append(1) # create a vector 
                else: l1.append(0) 
                if w in Y_set: l2.append(1) 
                else: l2.append(0) 
            c = 0
    
            # cosine formula  
            for i in range(len(rvector)): 
                c+= l1[i]*l2[i] 
            cosine = c / float((sum(l1)*sum(l2))**0.5) 
            #print("similarity: ", cosine) 
            list1.append(cosine)
            
            res_max = max(float(sub)*100 for sub in list1) 
        #print(str(res_max))
        print("Similarity percentage : " + str(res_max))
        if(res_max > 40):
            print("Sentence is similar")
        else:
            print("Sentence is not similar")   
        
        
b1 = tkinter.Button(text='Click to Convert file from mp3 to wav format', command=mp3_to_wav).pack()
b2 = tkinter.Button(text='Click to upload wav and text file', command=wav_text_up).pack()
tkinter.mainloop()
     

 
   
