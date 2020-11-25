from tkinter import *
import tkinter as tk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate('firebase-sdk.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://iteso-parking.firebaseio.com/'
})
ref = db.reference('/')


canvas = Canvas(0, width=1472, height=729)
frame = Frame(0, width=1008,height=100)
frame.pack()
canvas_iteso_logo = Canvas(0, width=224,height=182)
canvas_iteso_logo.pack()
img2 = PhotoImage(file='liteso.ppm')
canvas_iteso_logo.create_image(0,0,anchor=NW, image=img2)
img = PhotoImage(file='arboles.ppm')
canvas.create_image(0,0,anchor=NW, image=img)


canvas.pack()
def entry(txt):
    l=tk.Label(frame,text=txt,width=32)
    l.pack()
    e=tk.Entry(frame)
    e.pack()

state = entry("State")
Cajon = entry("Cajon")

canvas.create_window(700, 282, anchor=NW, window=frame)
canvas.create_window(700, 100, anchor='nw', window=canvas_iteso_logo)
canvas.mainloop()
