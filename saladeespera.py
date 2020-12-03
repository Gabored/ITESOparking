from tkinter import *
import tkinter as tk
import pyrebase
import random
config = {
  "apiKey": "AIzaSyA1ijWIJ8vBWiDNm7AV4ZC1Dk4UpHQUvqs",
  "authDomain": "iteso-parking.firebaseapp.com",
  "databaseURL": "https://iteso-parking.firebaseio.com",
  "storageBucket": "iteso-parking.appspot.com",
  "serviceAccount": "D:\Archivos  ITESO\Clases\Algoritmos y Programacion\ITESO Parking\ITESOparking\juan.json"
}








firebase = pyrebase.initialize_app(config)
db = firebase.database()
canvas = Canvas(0, width=1472, height=729)
frame = Frame(0, width=1008,height=100)
fr_leyenda = Frame(0)
fr_leyenda2 = Frame(0)
fr_leyenda3 = Frame(0)
fr_selected = Frame(0)
fr_ocupied= Frame(0)
fr_free = Frame(0)
fr_Logout = Frame(0)
fr_text = Frame(0, width=900,height=900)

canvas_parking = Canvas(0, width=560,height=400)
canvas_parking.pack()
img2 = PhotoImage(file='parkinglot.ppm')
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

boola1 = False
boola2 = False
boola3 = False
boola4 = False
boola5 = False
boola6 = False
boola7 = False
boola8 = False
boola9 = False
boola10 = False
boola11 = False
boola12 = False
boola13 = False
boola14 = False
boola15 = False


imga1 = PhotoImage(file=db.child("parking").child('A').child('A1').get().val())
imga2 = PhotoImage(file=db.child("parking").child('A').child('A2').get().val())
imga3 = PhotoImage(file=db.child("parking").child('A').child('A3').get().val())
imga4 = PhotoImage(file=db.child("parking").child('A').child('A4').get().val())
imga5 = PhotoImage(file=db.child("parking").child('A').child('A5').get().val())
imga6 = PhotoImage(file=db.child("parking").child('A').child('A6').get().val())
imga7 = PhotoImage(file=db.child("parking").child('A').child('A7').get().val())
imga8 = PhotoImage(file=db.child("parking").child('A').child('A8').get().val())
imga9 = PhotoImage(file=db.child("parking").child('A').child('A9').get().val())
imga10 = PhotoImage(file=db.child("parking").child('A').child('A10').get().val())
imga11 = PhotoImage(file=db.child("parking").child('A').child('A11').get().val())
imga12 = PhotoImage(file=db.child("parking").child('A').child('A12').get().val())
imga13 = PhotoImage(file=db.child("parking").child('A').child('A13').get().val())
imga14 = PhotoImage(file=db.child("parking").child('A').child('A14').get().val())
imga15 = PhotoImage(file=db.child("parking").child('A').child('A15').get().val())


def fbtn1():
    global boola1
    boola1 = True
    global boola2
    boola2 = False
    global boola3
    boola3 = False
    global boola4
    boola4 = False
    global boola5
    boola5 = False
    global boola6
    boola6 = False
    global boola7
    boola7 = False
    global boola8
    boola8 = False
    global boola9
    boola9 = False
    global boola10
    boola10 = False
    global boola11
    boola11 = False
    global boola12
    boola12 = False
    global boola13
    boola13 = False
    global boola14
    boola14 = False
    global boola15
    boola15 = False

    u['text']= 'A1'


def fbtn2():
    global boola1
    boola1 = False
    global boola2
    boola2 = True
    global boola3
    boola3 = False
    global boola4
    boola4 = False
    global boola5
    boola5 = False
    global boola6
    boola6 = False
    global boola7
    boola7 = False
    global boola8
    boola8 = False
    global boola9
    boola9 = False
    global boola10
    boola10 = False
    global boola11
    boola11 = False
    global boola12
    boola12 = False
    global boola13
    boola13 = False
    global boola14
    boola14 = False
    global boola15
    boola15 = False
    u['text']= 'A2'


def fbtn3():
    global boola1
    boola1 = False
    global boola2
    boola2 = False
    global boola3
    boola3 = True
    global boola4
    boola4 = False
    global boola5
    boola5 = False
    global boola6
    boola6 = False
    global boola7
    boola7 = False
    global boola8
    boola8 = False
    global boola9
    boola9 = False
    global boola10
    boola10 = False
    global boola11
    boola11 = False
    global boola12
    boola12 = False
    global boola13
    boola13 = False
    global boola14
    boola14 = False
    global boola15
    boola15 = False

    u['text']= 'A3'


def fbtn4():
    global boola1
    boola1 = False
    global boola2
    boola2 = False
    global boola3
    boola3 = False
    global boola4
    boola4 = True
    global boola5
    boola5 = False
    global boola6
    boola6 = False
    global boola7
    boola7 = False
    global boola8
    boola8 = False
    global boola9
    boola9 = False
    global boola10
    boola10 = False
    global boola11
    boola11 = False
    global boola12
    boola12 = False
    global boola13
    boola13 = False
    global boola14
    boola14 = False
    global boola15
    boola15 = False
    u['text']= 'A4'


def fbtn5():
    global boola1
    boola1 = False
    global boola2
    boola2 = False
    global boola3
    boola3 = False
    global boola4
    boola4 = False
    global boola5
    boola5 = True
    global boola6
    boola6 = False
    global boola7
    boola7 = False
    global boola8
    boola8 = False
    global boola9
    boola9 = False
    global boola10
    boola10 = False
    global boola11
    boola11 = False
    global boola12
    boola12 = False
    global boola13
    boola13 = False
    global boola14
    boola14 = False
    global boola15
    boola15 = False

    u['text']= 'A5'


def fbtn6():
    global boola1
    boola1 = False
    global boola2
    boola2 = False
    global boola3
    boola3 = False
    global boola4
    boola4 = False
    global boola5
    boola5 = False
    global boola6
    boola6 = True
    global boola7
    boola7 = False
    global boola8
    boola8 = False
    global boola9
    boola9 = False
    global boola10
    boola10 = False
    global boola11
    boola11 = False
    global boola12
    boola12 = False
    global boola13
    boola13 = False
    global boola14
    boola14 = False
    global boola15
    boola15 = False
    u['text']= 'A6'


def fbtn7():
    global boola1
    boola1 = False
    global boola2
    boola2 = False
    global boola3
    boola3 = False
    global boola4
    boola4 = False
    global boola5
    boola5 = False
    global boola6
    boola6 = False
    global boola7
    boola7 = True
    global boola8
    boola8 = False
    global boola9
    boola9 = False
    global boola10
    boola10 = False
    global boola11
    boola11 = False
    global boola12
    boola12 = False
    global boola13
    boola13 = False
    global boola14
    boola14 = False
    global boola15
    boola15 = False

    u['text']= 'A7'


def fbtn8():
    global boola1
    boola1 = False
    global boola2
    boola2 = False
    global boola3
    boola3 = False
    global boola4
    boola4 = False
    global boola5
    boola5 = False
    global boola6
    boola6 = False
    global boola7
    boola7 = False
    global boola8
    boola8 = True
    global boola9
    boola9 = False
    global boola10
    boola10 = False
    global boola11
    boola11 = False
    global boola12
    boola12 = False
    global boola13
    boola13 = False
    global boola14
    boola14 = False
    global boola15
    boola15 = False
    u['text']= 'A8'


def fbtn9():
    global boola1
    boola1 = False
    global boola2
    boola2 = False
    global boola3
    boola3 = False
    global boola4
    boola4 = False
    global boola5
    boola5 = False
    global boola6
    boola6 = False
    global boola7
    boola7 = False
    global boola8
    boola8 = False
    global boola9
    boola9 = True
    global boola10
    boola10 = False
    global boola11
    boola11 = False
    global boola12
    boola12 = False
    global boola13
    boola13 = False
    global boola14
    boola14 = False
    global boola15
    boola15 = False

    u['text']= 'A9'


def fbtn10():
    global boola1
    boola1 = False
    global boola2
    boola2 = False
    global boola3
    boola3 = False
    global boola4
    boola4 = False
    global boola5
    boola5 = False
    global boola6
    boola6 = False
    global boola7
    boola7 = False
    global boola8
    boola8 = False
    global boola9
    boola9 = False
    global boola10
    boola10 = True
    global boola11
    boola11 = False
    global boola12
    boola12 = False
    global boola13
    boola13 = False
    global boola14
    boola14 = False
    global boola15
    boola15 = False
    u['text']= 'A10'


def fbtn11():
    global boola1
    boola1 = False
    global boola2
    boola2 = False
    global boola3
    boola3 = False
    global boola4
    boola4 = False
    global boola5
    boola5 = False
    global boola6
    boola6 = False
    global boola7
    boola7 = False
    global boola8
    boola8 = False
    global boola9
    boola9 = False
    global boola10
    boola10 = False
    global boola11
    boola11 = True
    global boola12
    boola12 = False
    global boola13
    boola13 = False
    global boola14
    boola14 = False
    global boola15
    boola15 = False

    u['text']= 'A11'


def fbtn12():
    global boola1
    boola1 = False
    global boola2
    boola2 = False
    global boola3
    boola3 = False
    global boola4
    boola4 = False
    global boola5
    boola5 = False
    global boola6
    boola6 = False
    global boola7
    boola7 = False
    global boola8
    boola8 = False
    global boola9
    boola9 = False
    global boola10
    boola10 = False
    global boola11
    boola11 = False
    global boola12
    boola12 = True
    global boola13
    boola13 = False
    global boola14
    boola14 = False
    global boola15
    boola15 = False
    u['text']= 'A12'


def fbtn13():
    global boola1
    boola1 = False
    global boola2
    boola2 = False
    global boola3
    boola3 = False
    global boola4
    boola4 = False
    global boola5
    boola5 = False
    global boola6
    boola6 = False
    global boola7
    boola7 = False
    global boola8
    boola8 = False
    global boola9
    boola9 = False
    global boola10
    boola10 = False
    global boola11
    boola11 = False
    global boola12
    boola12 = False
    global boola13
    boola13 = True
    global boola14
    boola14 = False
    global boola15
    boola15 = False

    u['text']= 'A13'


def fbtn14():
    global boola1
    boola1 = False
    global boola2
    boola2 = False
    global boola3
    boola3 = False
    global boola4
    boola4 = False
    global boola5
    boola5 = False
    global boola6
    boola6 = False
    global boola7
    boola7 = False
    global boola8
    boola8 = False
    global boola9
    boola9 = False
    global boola10
    boola10 = False
    global boola11
    boola11 = False
    global boola12
    boola12 = False
    global boola13
    boola13 = False
    global boola14
    boola14 = True
    global boola15
    boola15 = False
    u['text']= 'A14'


def fbtn15():
    global boola1
    boola1 = False
    global boola2
    boola2 = False
    global boola3
    boola3 = False
    global boola4
    boola4 = False
    global boola5
    boola5 = False
    global boola6
    boola6 = False
    global boola7
    boola7 = False
    global boola8
    boola8 = False
    global boola9
    boola9 = False
    global boola10
    boola10 = False
    global boola11
    boola11 = False
    global boola12
    boola12 = False
    global boola13
    boola13 = False
    global boola14
    boola14 = False
    global boola15
    boola15 = True

    u['text']= 'A15'
def logOut():
    dr = db.child("active").child('boton').get().val()
    jayson = \
        {
            dr: 'brojo.ppm'
        }
    db.child('parking').child('A').update(jayson)
    db.child("active").update({'usuario': ''})
    db.child("active").update({'boton': ''})
def isOcupied():
    checkBool()
    jayson = \
        {
            dr: 'brojo.ppm'
        }
    db.child('parking').child('A').update(jayson)
def isFree():
    checkBool()
    jayson = \
        {
            dr: 'bverde.ppm'
        }
    db.child('parking').child('A').update(jayson)
def checkBool():
    global dr
    if boola1 == True and boola2 == False and boola3 == False and boola4 == False and boola5 == False and boola6 == False and boola7 == False and boola8 == False and boola9 == False and boola10 == False and boola11 == False and boola12 == False and boola13 == False and boola14 == False and boola15 == False:
        print("A1 True")
        dr = 'A1'
    if boola1 == False and boola2 == True and boola3 == False and boola4 == False and boola5 == False and boola6 == False and boola7 == False and boola8 == False and boola9 == False and boola10 == False and boola11 == False and boola12 == False and boola13 == False and boola14 == False and boola15 == False:
        print("A2 True")
        dr = 'A2'
    if boola1 == False and boola2 == False and boola3 == True and boola4 == False and boola5 == False and boola6 == False and boola7 == False and boola8 == False and boola9 == False and boola10 == False and boola11 == False and boola12 == False and boola13 == False and boola14 == False and boola15 == False:
        print("A3 True")
        dr = 'A3'
    if boola1 == False and boola2 == False and boola3 == False and boola4 == True and boola5 == False and boola6 == False and boola7 == False and boola8 == False and boola9 == False and boola10 == False and boola11 == False and boola12 == False and boola13 == False and boola14 == False and boola15 == False:
        print("A4 True")
        dr = 'A4'
    if boola1 == False and boola2 == False and boola3 == False and boola4 == False and boola5 == True and boola6 == False and boola7 == False and boola8 == False and boola9 == False and boola10 == False and boola11 == False and boola12 == False and boola13 == False and boola14 == False and boola15 == False:
        print("A5 True")
        dr = 'A5'
    if boola1 == False and boola2 == False and boola3 == False and boola4 == False and boola5 == False and boola6 == True and boola7 == False and boola8 == False and boola9 == False and boola10 == False and boola11 == False and boola12 == False and boola13 == False and boola14 == False and boola15 == False:
        print("A6 True")
        dr = 'A6'
    if boola1 == False and boola2 == False and boola3 == False and boola4 == False and boola5 == False and boola6 == False and boola7 == True and boola8 == False and boola9 == False and boola10 == False and boola11 == False and boola12 == False and boola13 == False and boola14 == False and boola15 == False:
        print("A7 True")
        dr = 'A7'
    if boola1 == False and boola2 == False and boola3 == False and boola4 == False and boola5 == False and boola6 == False and boola7 == False and boola8 == True and boola9 == False and boola10 == False and boola11 == False and boola12 == False and boola13 == False and boola14 == False and boola15 == False:
        print("A8 True")
        dr = 'A8'
    if boola1 == False and boola2 == False and boola3 == False and boola4 == False and boola5 == False and boola6 == False and boola7 == False and boola8 == False and boola9 == True and boola10 == False and boola11 == False and boola12 == False and boola13 == False and boola14 == False and boola15 == False:
        print("A9 True")
        dr = 'A9'
    if boola1 == False and boola2 == False and boola3 == False and boola4 == False and boola5 == False and boola6 == False and boola7 == False and boola8 == False and boola9 == False and boola10 == True and boola11 == False and boola12 == False and boola13 == False and boola14 == False and boola15 == False:
        print("A10 True")
        dr = 'A10'
    if boola1 == False and boola2 == False and boola3 == False and boola4 == False and boola5 == False and boola6 == False and boola7 == False and boola8 == False and boola9 == False and boola10 == False and boola11 == True and boola12 == False and boola13 == False and boola14 == False and boola15 == False:
        print("A11 True")
        dr = 'A11'
    if boola1 == False and boola2 == False and boola3 == False and boola4 == False and boola5 == False and boola6 == False and boola7 == False and boola8 == False and boola9 == False and boola10 == False and boola11 == False and boola12 == True and boola13 == False and boola14 == False and boola15 == False:
        print("A12 True")
        dr = 'A12'
    if boola1 == False and boola2 == False and boola3 == False and boola4 == False and boola5 == False and boola6 == False and boola7 == False and boola8 == False and boola9 == False and boola10 == False and boola11 == False and boola12 == False and boola13 == True and boola14 == False and boola15 == False:
        print("A13 True")
        dr = 'A13'
    if boola1 == False and boola2 == False and boola3 == False and boola4 == False and boola5 == False and boola6 == False and boola7 == False and boola8 == False and boola9 == False and boola10 == False and boola11 == False and boola12 == False and boola13 == False and boola14 == True and boola15 == False:
        print("A14 True")
        dr = 'A14'
    if boola1 == False and boola2 == False and boola3 == False and boola4 == False and boola5 == False and boola6 == False and boola7 == False and boola8 == False and boola9 == False and boola10 == False and boola11 == False and boola12 == False and boola13 == False and boola14 == False and boola15 == True:
        print("A15 True")
        dr = 'A15'


a1 =tk.Button(btn1, image=imga1, command=fbtn1).pack()
a2 =tk.Button(btn2, image=imga2, command=fbtn2).pack()
a3 =tk.Button(btn3, image=imga3, command=fbtn3).pack()
a4 =tk.Button(btn4, image=imga4, command=fbtn4).pack()
a5 =tk.Button(btn5,image=imga5, command=fbtn5).pack()
a6 =tk.Button(btn6,image=imga6, command=fbtn6).pack()
a7 =tk.Button(btn7,image=imga7, command=fbtn7).pack()
a8 =tk.Button(btn8,image=imga8, command=fbtn8).pack()
a9 =tk.Button(btn9,image=imga9, command=fbtn9).pack()
a10 =tk.Button(btn10,image=imga10, command=fbtn10).pack()
a11 =tk.Button(btn11,image=imga11, command=fbtn11).pack()
a12 =tk.Button(btn12,image=imga12, command=fbtn12).pack()
a13 =tk.Button(btn13,image=imga13, command=fbtn13).pack()
a14 =tk.Button(btn14,image=imga14, command=fbtn14).pack()
a15 =tk.Button(btn15,image=imga15, command=fbtn15).pack()

btn_ocupied = tk.Button(fr_ocupied, text='Ocupado',  width=35, command= isOcupied)
btn_ocupied.pack()
btn_free = tk.Button(fr_free, text='Free',  width=35, command = isFree)
btn_free.pack()
btn_logout = tk.Button(fr_Logout, text=' Log Out ', width=35, command = logOut)
btn_logout.pack()
k = Text(fr_text,width=80, height=10)
k.insert(INSERT, "Este es el espacio proporcionado para que usted coloque los datos de los 3 cajones en gris cercanos a usted, por favor seleccionelos y despues haga click en ocupado o libre segun su estado. Si localizas algun espacio que se encuntra mal sientete libre de corregirlo ")
k.pack()
y = tk.Label(fr_leyenda, text='Leyenda: Verde es Libre  Naranja es Reservado, Rojo es ocupado, Gris es desahibiltado ', width=70, height= 2, font=('Helvetica', 10))
y.pack()
entry("Bienvenido a la sala de espera ")
t = tk.Label(fr_leyenda2, text=' Mapa Estacionamiento', width=70, height= 2, font=('Helvetica', 10))
t.pack()
u= tk.Label(fr_selected, text= '',  width= 5, height= 2, font=('Helvetica', 10))
z = tk.Label(fr_leyenda3, text='Lugar Seleccionado : ', width=70, height= 2, font=('Helvetica', 10))
z.pack()
u.pack()
canvas.create_window(127, 180, anchor='nw', window=fr_leyenda)
canvas.create_window(127, 140, anchor='nw', window=fr_leyenda2)
canvas.create_window(820, 160, anchor='nw', window=fr_leyenda3)
canvas.create_window(1200, 160, anchor='nw', window=fr_selected)
canvas.create_window(130, 220, anchor='nw', window=canvas_parking)
canvas.create_window(130, 280, anchor=NW, window=btn1)
canvas.create_window(190,280, anchor= NW, window=btn2)
canvas.create_window(250,280, anchor= NW, window=btn3)
canvas.create_window(310,280, anchor= NW, window=btn4)
canvas.create_window(375,280, anchor= NW, window=btn5)
canvas.create_window(435,280, anchor= NW, window=btn6)
canvas.create_window(495,280, anchor= NW, window=btn7)
canvas.create_window(560,280, anchor= NW, window=btn8)
canvas.create_window(620,280, anchor= NW, window=btn9)
canvas.create_window(560,420, anchor= NW, window=btn10)
canvas.create_window(560,486, anchor= NW, window=btn11)
canvas.create_window(560,550, anchor= NW, window=btn12)
canvas.create_window(190,550, anchor= NW, window=btn13)
canvas.create_window(190,486, anchor= NW, window=btn14)
canvas.create_window(190,420, anchor= NW, window=btn15)
canvas.create_window(1200, 500, anchor= 'nw', window=fr_Logout)
canvas.create_window(10, 10, anchor='nw', window=frame)
canvas.create_window(860, 400, anchor='nw', window=fr_ocupied)
canvas.create_window(1100, 400, anchor='nw', window=fr_free)
canvas.create_window(800,200, anchor='nw', window=fr_text)
canvas.mainloop()