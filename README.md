# E-Learning-System-for-Detection-of-Learning-Disability


# Use Python Anaconda Distribution
# Packages to be installed
pip install SpeechRecognition
pip install pydub
# packages for semantics
pip install wordcloud

# To Run python files:
python filename.py on command prompt

# Common Procedure for file conversion
Run conversion.py in file conversions folder to convert either files from m4a to mp3 format or from mp3 to wav format.

# Miscue
First run either miscue_add.py or miscue_omit.py. Run miscue_rem.py in the end and use the switch case 'ps' in this file after the cases 's','r' & 'm'.
In all the miscue files, either mp3 to wav conversion can be done or directly .wav file can be uploaded (for audio input) followed by the corresponding grade .txt file (for corpus)

# picture description & sequence
When running picture.py or sequence.py the same file conversion method provided as that in the miscue files. Instead directly .wav file can also be uploaded followed by the corresponding corpus.

# topic description (essay)
For Essay.py directly .txt file has to be uploaded first (for corpus). Here, the word cloud and the bar graph is generated. This to be followed by the uploading the .wav file (audio).


 
