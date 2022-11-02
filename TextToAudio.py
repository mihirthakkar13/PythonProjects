# gTTS is a very easy to use tool which converts the text entered,
# # into audio which can be saved as a mp3 file

from gtts import gTTS
#pip install gtt

#playsound is a Python module by which users can play sound in a single line of code.

from playsound import playsound
#pip install playsound

audio = 'Example.mp3'

language = 'en'

sp = gTTS(text = "Hello Everyone. Myself Mihir Thakkar and Welcome to this project. ", lang = language , 
        slow= False)
sp.save(audio)

playsound(audio)
