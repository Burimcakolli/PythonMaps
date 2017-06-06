from tkinter import Tk, Label, Button, Text, END
from tkinter import ttk





class MyFirstGUI:

    def __init__(self, master):
        bg_colour = '#5c5e5d'

        self.master = master
        master.title("A simple GUI")
        master.minsize(width=250, height=150)
        master.maxsize(width=666, height=666)
        self.t = Text(root, height=2, width=30)
        self.t.pack(pady=2)
        T = Text(root, height=2, width=30)
        T.pack(pady=2)

        self.greet_button = ttk.Button(master, text="Strecke ausrechnen", command = self.ausrechnen)
        self.greet_button.pack()
        self.label_strecke = Label(master, text="hier wird die Strecke angezeigt")
        self.label_strecke.pack()


    def ausrechnen(self):
        self.label_strecke['text'] = "Name der 1. Stadt: " + self.t.get("1.0",END)
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()