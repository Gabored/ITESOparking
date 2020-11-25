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
fr_leyenda = Frame(0)
fr_text = Frame(0, width=900,height=900)
fr_button = Frame(0, width=50,height=100)
fr_button_2 = Frame(0, width=50,height=100)
canvas_parking = Canvas(0, width=560,height=400)
canvas_parking.pack()
img3 = PhotoImage(file='barrow.ppm')
img4 = PhotoImage(file='barrow-r.ppm')
img2 = PhotoImage(file='parkinglot.ppm')
canvas_parking.create_image(0,0,anchor=NW, image=img2)
img = PhotoImage(file='arboles.ppm')
canvas.create_image(0,0,anchor=NW, image=img)

canvas.pack()
def entry(txt):
    l=tk.Label(frame,text=txt,width=90,height=2,font=('Helvetica', 20))
    l.pack()
bizq =tk.Button(fr_button, image=img3)
bizq.pack()
bir =tk.Button(fr_button_2, image=img4)
bir.pack()
k = Text(fr_text,width=80, height=10)
k.insert(INSERT, "Recuerda que la opción de reservar un cajón se encuentra disponible para los estudiantes que están dispuestos a que al llegar a la universidad otorguen a la aplicación el estado(Vacio, ocupado) de tres cajones que el sistema tenga etiquetados como sin información. Entendemos que si usted no desea otorgar dicha información se limite a mirar en el mapa que lugares están disponibles para posteriormente cuando llegue, marcarlo como ocupado. El no respetar esta normativa y reservar su espacio sin otorgar al sistema la información en un máximo de 30 min después de su llegada a la institución le hará acreedor de una sanción del uso de la funcionabilidad de Reservar por una semana.El propósito de esta herramienta es que sea para un beneficio de la comunidad, le exhortamos a no abusar de ella")
k.pack()
y = tk.Label(fr_leyenda, text='Leyenda:', width=30, height= 2, font=('Helvetica', 20))
y.pack
entry("Elige un Lugar de Estacionamiento en el mapoide")
canvas.create_window(80, 100, anchor='nw', window=fr_leyenda)
canvas.create_window(80, 350, anchor='nw', window=fr_button)
canvas.create_window(690, 350, anchor='nw', window=fr_button_2)
canvas.create_window(130, 220, anchor='nw', window=canvas_parking)
canvas.create_window(10, 10, anchor='nw', window=frame)
canvas.create_window(800,200, anchor='nw', window=fr_text)
canvas.mainloop()