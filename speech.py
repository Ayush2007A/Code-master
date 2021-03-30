import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices['Microsoft Zira'].id)  # use whatever voice_id you'd like
engine.say('a')
engine.runAndWait()
