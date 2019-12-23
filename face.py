from tkinter import *
from main import char

root = Tk()
root.title("DnD5 char gen")
root.geometry("1280x700+300+300")

label = Text(width=1200)
label.pack(side=LEFT, padx=0, pady=0)

ttk.Button(root, text='Сгенерировать персонажа', width=15,command=char).pack(side=RIGHT, padx=5, pady=5)

root.mainloop()
