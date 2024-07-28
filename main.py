import os
import pyttsx3

if __name__=='__main__':
    print("Welcome to RoboSpeaker 1.1. Create by Naimur")
    while True:
        x=input("Enter what you want me to speak: ")
        if x=='q':
            engine = pyttsx3.init()
            engine.say("Bye Bye friend")
            engine.runAndWait()
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()

    # os.system(command)

