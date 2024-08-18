#install pyttsx3 packege
#install pywin32 packege

from tkinter import *
import pyttsx3

root=Tk()
root.geometry("600x300")
root.title("Speaking Software")
root.configure(background="blue")
root.maxsize(600,300)
root.minsize(600,300)
#Functions
def speak(event):

#Use of pytts3 packege
    engine=pyttsx3.init()
    #control speaking speed
    engine.setProperty('rate', 125)

    #Control volume
    new_volume=volume.get()/10
    engine.setProperty('volume',new_volume)

    #Set woman voice
    voices = engine.getProperty('voices')    #getting details of current voice
    engine.setProperty('voice', voices[1].id)

    engine.say(entry.get())
    engine.runAndWait()
    #entry.delete(0,END)
#Body

Label(root,text="Write to speak",font="Algerian 25 underline",bg="blue",fg="white").place(x=140,y=20)
entry=Entry(root,font="calibri 16",width=40)
entry.place(x=40,y=100)
button=Button(root,text="Speak",font="calibri 20",width=15)
button.place(x=150,y=160)
button.bind('<Button-1>',speak)
Label(root,text="Volume",font="calibri 12 bold",bg="blue",fg="white").place(x=530,y=20)
volume=Scale(root,bg="light blue",from_=0,to=10,length=230,borderwidth=0,relief=SUNKEN)
volume.place(x=536,y=50)


root.mainloop()