from tkinter import *
import tkinter as tk
import pyrebase
config = {
  "apiKey": "AIzaSyA1ijWIJ8vBWiDNm7AV4ZC1Dk4UpHQUvqs",
  "authDomain": "iteso-parking.firebaseapp.com",
  "databaseURL": "https://iteso-parking.firebaseio.com",
  "storageBucket": "iteso-parking.appspot.com",
  "serviceAccount": "E:\GitHub\ITESOparking\juan.json"
}
firebase = pyrebase.initialize_app(config)
active_user = ''
db = firebase.database()
all_users = db.child("Usuarios").get()
def logIn(usr, passw):

    for user in all_users.each():
        if usr == str(user.key()):
            if passw == user.val().get('password'):
                print("Log exitoso")
                active_user = usr
                return True
            else:
                return False



print(logIn("gabo","Chucxhitsa"))
canvas = Canvas(0, width=1472, height=729)
frame = Frame(0, width=1008,height=100)
fr_leyenda = Frame(0)
fr_leyenda2 = Frame(0)
fr_leyenda3 = Frame(0)
btn_frame = Frame(0)
fr_text = Frame(0, width=900,height=900)
fr_button = Frame(0, width=50,height=100)
fr_button_2 = Frame(0, width=50,height=100)
canvas_parking = Canvas(0, width=560,height=400)
canvas_parking.pack()
img3 = PhotoImage(file='barrow.ppm')
img4 = PhotoImage(file='barrow-r.ppm')
img2 = PhotoImage(file='parkinglot.ppm')
img5 = PhotoImage(file='elbueno.ppm')
canvas_parking.create_image(0,0,anchor=NW, image=img2)
img = PhotoImage(file='arboles.ppm')
canvas.create_image(0,0,anchor=NW, image=img)
btn1= Frame(0,width=200,height=200)
btn2= Frame(0,width=200,height=200)
btn3= Frame(0,width=200,height=200)
btn4= Frame(0,width=200,height=200)
btn5= Frame(0,width=200,height=200)
btn6= Frame(0,width=200,height=200)
btn7= Frame(0,width=200,height=200)
btn8= Frame(0,width=200,height=200)
btn9= Frame(0,width=200,height=200)
btn10= Frame(0,width=200,height=200)
btn11= Frame(0,width=200,height=200)
btn12= Frame(0,width=200,height=200)
btn13= Frame(0,width=200,height=200)
btn14= Frame(0,width=200,height=200)
btn15= Frame(0,width=200,height=200)
canvas.pack()
def entry(txt):
    l=tk.Label(frame,text=txt,width=90,height=2,font=('Helvetica', 20))
    l.pack()
a1 =tk.Button(btn1,image=img5)
a1.pack()
a2 =tk.Button(btn2,image=img5).pack()
a3 =tk.Button(btn3,image=img5).pack()
a4 =tk.Button(btn4,image=img5).pack()
a5 =tk.Button(btn5,image=img5).pack()
a6 =tk.Button(btn6,image=img5).pack()
a7 =tk.Button(btn7,image=img5).pack()
a8 =tk.Button(btn8,image=img5).pack()
a9 =tk.Button(btn9,image=img5).pack()
a10 =tk.Button(btn10,image=img5).pack()
a11 =tk.Button(btn11,image=img5).pack()
a12 =tk.Button(btn12,image=img5).pack()
a13 =tk.Button(btn13,image=img5).pack()
a14 =tk.Button(btn14,image=img5).pack()
a15 =tk.Button(btn15,image=img5).pack()


bizq =tk.Button(fr_button, image=img3)
bizq.pack()
bir =tk.Button(fr_button_2, image=img4)
bir.pack()
btn_reserve = tk.Button(btn_frame, text='Reservar', state= DISABLED, width=70)
btn_reserve.pack()
k = Text(fr_text,width=80, height=10)
k.insert(INSERT, "Recuerda que la opción de reservar un cajón se encuentra disponible para los estudiantes que están dispuestos a que al llegar a la universidad otorguen a la aplicación el estado(Vacio, ocupado) de tres cajones que el sistema tenga etiquetados como sin información. Entendemos que si usted no desea otorgar dicha información se limite a mirar en el mapa que lugares están disponibles para posteriormente cuando llegue, marcarlo como ocupado. El no respetar esta normativa y reservar su espacio sin otorgar al sistema la información en un máximo de 30 min después de su llegada a la institución le hará acreedor de una sanción del uso de la funcionabilidad de Reservar por una semana.El propósito de esta herramienta es que sea para un beneficio de la comunidad, le exhortamos a no abusar de ella")
k.pack()
y = tk.Label(fr_leyenda, text='Leyenda: Verde es Libre  Naranja es Reservado, Rojo es ocupado, Gris es desahibiltado ', width=70, height= 2, font=('Helvetica', 10))
y.pack()
entry("Elige un Lugar de Estacionamiento en el mapa")
t = tk.Label(fr_leyenda2, text=' Mapa Zona A', width=70, height= 2, font=('Helvetica', 10))
t.pack()
z = tk.Label(fr_leyenda3, text='Lugar Seleccionado : A1 ', width=70, height= 2, font=('Helvetica', 10))
z.pack()

canvas.create_window(127, 180, anchor='nw', window=fr_leyenda)
canvas.create_window(127, 140, anchor='nw', window=fr_leyenda2)
canvas.create_window(820, 160, anchor='nw', window=fr_leyenda3)
canvas.create_window(80, 350, anchor='nw', window=fr_button)
canvas.create_window(690, 350, anchor='nw', window=fr_button_2)
canvas.create_window(130, 220, anchor='nw', window=canvas_parking)
canvas.create_window(10,400, anchor='nw', window=btn1)
canvas.create_window(130,300, anchor= NW, window=btn2)
canvas.create_window(130,300, anchor= NW, window=btn3)
canvas.create_window(130,300, anchor= NW, window=btn4)
canvas.create_window(130,300, anchor= NW, window=btn5)
canvas.create_window(130,300, anchor= NW, window=btn6)
canvas.create_window(130,300, anchor= NW, window=btn7)
canvas.create_window(130,300, anchor= NW, window=btn8)
canvas.create_window(130,300, anchor= NW, window=btn9)
canvas.create_window(130,300, anchor= NW, window=btn10)
canvas.create_window(130,300, anchor= NW, window=btn11)
canvas.create_window(130,300, anchor= NW, window=btn12)
canvas.create_window(130,300, anchor= NW, window=btn13)
canvas.create_window(130,300, anchor= NW, window=btn14)
canvas.create_window(130,300, anchor= NW, window=btn15)

canvas.create_window(10, 10, anchor='nw', window=frame)
canvas.create_window(860, 400, anchor='nw', window=btn_frame)
canvas.create_window(800,200, anchor='nw', window=fr_text)
canvas.mainloop()