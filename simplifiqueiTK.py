from tkinter import *
from tkinter import ttk


#SIMPLIFIQUEI SÓ PRA VER NO Q DÁ

frm = ttk.Frame(Tk(), padding=10)

frm.grid()


ttk.Label(frm, text= " Hello World!").grid(column=0, row=0)


ttk.Button(frm, text= "Quit", command=Tk().destroy).grid(column=1, row=0)


Tk().mainloop()


#DÁ MUITA MERDA