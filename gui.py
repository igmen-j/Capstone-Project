from guizero import *
import os

def startScript():
    os.system('python my_file.py')

def stopScript():
    os.system('pkill -9 -f my_file.py')

app = App(title="Project", bg="black")
start = PushButton(app, command=startScript, text="Start",  width=20, height=5, align="left")
start.bg = "Green"
start.tk.config(font=("Impact", 15))

stop = PushButton(app, command=stopScript, text="Stop",  width=20, height=5, align="right")
stop.bg = "Red"
stop.tk.config(font=("Impact", 15))

app.display()
