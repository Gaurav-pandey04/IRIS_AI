import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import openai
import subprocess



#Response voice of IRIS AI
engine = pyttsx3.init()
#voice and other property of engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # set the first available voice
engine.setProperty('rate', 150)  # set the speaking rate (words per minute)
engine.setProperty('volume', 1.0)  # set the volume (0.0 to 1.0)
#speacking property of IRIS AI
engine.say("Starting System")
print("Starting System")
engine.say("Hello, I am IRIS an A I. How May I help you?")
print("Hello, I am IRIS an A I. How May I help you?")
engine.runAndWait()


OPENAI_API_KEY=	"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"
def openAi( question):
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"User: {question} /n IRIS: ",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    try:
        print("IRIS: " ,response["choices"][0]["text"])
        engine.say(response["choices"][0]["text"])
        engine.runAndWait()
    except ValueError as e:
        engine.say("Something went wrong")
        engine.runAndWait()


while True:
    #listening the voice from user
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    
    query = r.recognize_google(audio)
    print("Gaurav: ", query)
    # engine.say(text)
    sites = [['youtube', 'https://www.youtube.com/'], ['google', 'http://www.google.com'], ['Instagram','https://www.instagram.com/'], ['twitter', 'https://twitter.com/']]
    if "open" in query:
        if "app" in query:
            app_path = "C:\\Program Files\\Internet Explorer\\iexplore.exe"  # path to the application
            subprocess.Popen(app_path)  # open the application
        
        else:
            for site in sites:
                if f"open {site[0]}".lower() in query.lower():
                    engine.say(f"opening {site[0]} sir....")
                    engine.runAndWait()
                    webbrowser.open(site[1])

        

    elif "quit" in query:
        engine.say("System Shutdown")
        print("System Shutdown")
        engine.runAndWait()
        exit()
    
    else:
        openAi(query) 
