import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good moorning')

    elif hour>=12 and hour<18:
        speak('good afternoon')
    else:
        speak('good evening')
    speak('i am friday sir may help you')
def takecomand():
    """ take argument"""
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold =1
        audio=r.listen(source)
    try:
        print('Recognizing....')
        query=r.recognize_google(audio, language='en-in',show_all=False)
        print(" User said:", query)


    except Exception as e:
        # print(e)
        print("say that again please....")
        return "None"
    return query

if __name__ == '__main__':
    wishme()
    while True:
        quary=takecomand().lower()
        if 'wikipedia' in quary:
            speak("searching wikipidia...")
            quary=quary.replace("wikipedia", "")
            results=wikipedia.summary(quary, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif'open youtube' in quary:
            webbrowser.open("youtube.com")
        elif'open stackoverflow' in quary:
            webbrowser.open('stakoverflow.com')
        elif'play music' in quary:
            music_dir='E:\\UCDownloads'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif'open gmail' in quary:
            webbrowser.open('gmail.com')
        elif (["search"]) and 'youtube' not in quary:
            search_term = voice_data.replace("search","")
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            # engine_speak("Here is what I found for" + search_term + "on google")





