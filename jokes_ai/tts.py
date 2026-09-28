import pyttsx4

#initialize engine
engine = pyttsx4.init()

#optional:adjust speech rate and volume
engine.setProperty('rate', 175) #speed (words per minute)
engine.setProperty('volume',0.9) #volume (0.0 to 1.0)

#speak text 
engine.say('Hello! this works offline without an internet connection.')
engine.runAndWait()

#clean up explicitly befoe exit
engine.stop()
del engine