from tkinter import *
import subprocess

def setButton(show):
    show.button = Button(text="Stop all containers")
    show.button.pack()

def stopAllRunningContainers():
    process = subprocess.Popen(["docker", "ps", "-q"], stdout=subprocess.PIPE)
    out, err = process.communicate()
    print(out.decode('utf8'))
