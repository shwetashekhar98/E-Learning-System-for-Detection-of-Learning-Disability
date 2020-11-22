import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import collections
import numpy as np
import pandas as pd
import matplotlib.cm as cm
from matplotlib import rcParams
import nltk
#nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import speech_recognition as sr
import os
from tkinter import filedialog
from os import path
from pydub import AudioSegment
import tkinter

def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = int(360.0 * 45.0 / 255.0)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(random_state.randint(60, 120)) / 255.0)

    return "hsl({}, {}%, {}%)".format(h, s, l)

file_content=filedialog.askopenfilename(initialdir = "/home/shweta/Desktop/", title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
file_content=open(file_content).read()
file_content=file_content.lower()
wordcloud = WordCloud(
                            stopwords = STOPWORDS,
                            background_color = 'white',
                            width = 1200,
                            height = 1000,
                            color_func = random_color_func




                  ).generate(file_content)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()
stopwords=STOPWORDS
stopwords=['will','us','I','We','She','all.','way.','subject.','my','way.','But'] + list(STOPWORDS)
filtered_words = [word for word in file_content.split() if word not in stopwords]
counted_words = collections.Counter(filtered_words)

words = []
counts = []
for letter, count in counted_words.most_common(100):
    words.append(letter)
    counts.append(count)
colors = cm.rainbow(np.linspace(0, 1, 10))
rcParams['figure.figsize'] = 40, 50

plt.title('Top words in the corpus vs their count')
plt.xlabel('Count')
plt.ylabel('Words')
plt.barh(words, counts, color=colors)
plt.show()
item=[]
for item_a, item_b in zip(words,counts):
    a=item_a,item_b
    item.append(item_a)
r = sr.Recognizer()
filename2 =  filedialog.askopenfilename(initialdir = "C:/Users/Shweta/Documents/Sound recordings", title = "Select file",filetypes = (("wav files","*.wav"),("all files","*.*")))
file_audio = sr.AudioFile(filename2)
with file_audio as source:
    audio = r.record(source)
    try:
        get = r.recognize_google(audio)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed'.format(e))
print(get)

X = get.lower()

# tokenization
X_list = word_tokenize(X)

# sw contains the list of stopwords
sw = STOPWORDS
l1 =[];l2 =[]

# remove stop words from string
X_set = {w for w in X_list if not w in sw}
print(X_set)
item=set(item)
print(item)
# form a set containing keywords of both strings
rvector = X_set.union(item)
for w in rvector:
    if w in X_set: l1.append(1) # create a vector
    else: l1.append(0)
    if w in item: l2.append(1)
    else: l2.append(0)
c = 0

# cosine formula
for i in range(len(rvector)):
        c+= l1[i]*l2[i]
cosine = c / float((sum(l1)*sum(l2))**0.5)
print("similarity: ", cosine)

if(cosine < 0.1):
    print("The sentence is not sensible")
elif(cosine >= 0.1):
    print("The sentence is sensible")









