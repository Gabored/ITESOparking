from tkinter import *
import tkinter as tk
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import db
#cred = credentials.Certificate('firebase-sdk.json')
#firebase_admin.initialize_app(cred, {
#    'databaseURL' : 'https://iteso-parking.firebaseio.com/'
#})
#ref = db.reference('/')


canvas = Canvas(0, width=1472, height=729)
frame = Frame(0, width=1008,height=100)
canvas_button = Canvas(0, width=50,height=100)
canvas_parking = Canvas(0, width=560,height=400)
canvas_parking.pack()
img3 = PhotoImage(file='barrow.ppm')
img2 = PhotoImage(file='parkinglot.ppm')
canvas_parking.create_image(0,0,anchor=NW, image=img2)
img = PhotoImage(file='arboles.ppm')
canvas.create_image(0,0,anchor=NW, image=img)
canvas_button.create_image(0,0,anchor=NW,image=img3)
canvas.pack()
def entry(txt):
    l=tk.Label(frame,text=txt,width=90,height=2,font=('Helvetica', 20))
    l.pack()
bizq =tk.Button()

entry("Elige un Lugar de Estacionamiento en el mapa")
canvas.create_window(30, 350, anchor='nw', window=canvas_button)
canvas.create_window(130, 220, anchor='nw', window=canvas_parking)
canvas.create_window(10, 10, anchor='nw', window=frame)
canvas.mainloop()