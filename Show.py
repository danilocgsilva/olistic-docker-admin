from tkinter import *
from fn import *


class Show:

    def __init__(self, instance):
        instance.geometry("600x300")
        self.fr1 = Frame(instance)
        self.fr1.pack()

        setButton(self)