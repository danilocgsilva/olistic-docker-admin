from olistic_docker_admin.fn import *

class Show:

    def __init__(self, instance):
        instance.title("Docker GUI admin")
        instance.geometry("600x300+200+200")
        self.fr1 = Frame(instance)
        self.fr1.pack(padx=20, pady=20)

        setButton(self)
