from tkinter import *
from tkinter import messagebox
top = Tk()

C = Canvas(top, bg="blue", height=250, width=300)
filename = PhotoImage(file = 'arboles.ppm')
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
j = Label(top,text = "Password",width=32).pack()
e=Entry(top,show="*",text = "Password",width=32).pack()

C.pack()
top.mainloop()