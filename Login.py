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
db = firebase.database()
active_user = ''
all_users = db.child("Usuarios").get()

json ={
  "Usuarios" : {
      "Juan" : {
          "password": "naruto69"
      }
  },
  "active" : {
    "usuario" : ""
  },
  "parking" : {
    "A" : {
      "A1" : "bgris.ppm",
      "A10" : "bgris.ppm",
      "A11" : "bgris.ppm",
      "A12" : "bgris.ppm",
      "A13" : "bgris.ppm",
      "A14" : "bgris.ppm",
      "A15" : "bgris.ppm",
      "A2" : "bgris.ppm",
      "A3" : "bgris.ppm",
      "A4" : "bgris.ppm",
      "A5" : "bgris.ppm",
      "A6" : "bgris.ppm",
      "A7" : "bgris.ppm",
      "A8" : "bgris.ppm",
      "A9" : "bgris.ppm"
    }
  }
}
db.set(json)

#Funcion para boton de Login
def logIn():
    usr = userio.get()
    passw = password.get()

    for user in all_users.each():
        if usr == str(user.key()):
            if passw == user.val().get('password'):

                json = {
                    usr:''
                }
                db.child("active").set(json)
                labellog["text"] = "Log exitoso"
                return True
            else:

                labellog["text"] = "El usuario o la contraseña son incorrectos"
                return False

        labellog["text"] = "El usuario o la contraseña son incorrectos"



canvas = Canvas(0, width=1472, height=729)
frame = Frame(0, width=1008,height=500)
frame.pack()
canvas_iteso_logo = Canvas(0, width=224,height=182)
canvas_iteso_logo.pack()
img2 = PhotoImage(file='liteso.ppm')
canvas_iteso_logo.create_image(0,0,anchor=NW, image=img2)
img = PhotoImage(file='arboles.ppm')
canvas.create_image(0,0,anchor=NW, image=img)

canvas.pack()

userio =tk.StringVar()
password = tk.StringVar()

#Funcion de entrada de texto
def entry(txt):
    l=tk.Label(frame,text=txt,width=32)
    l.pack()
    e = tk.Entry(frame,text=txt,width=32,textvariable = userio)
    e.pack()



user = entry("Username")

j = tk.Label(frame,text = "Password",width=32).pack()
e=tk.Entry(frame,show="*",text = "Password",width=32,textvariable = password).pack()
button =tk.Button(frame,text="Login", command = logIn)
button.pack()
signbutton =tk.Button(frame,text="Sign Up")
signbutton.pack()

labellog = Label(frame)
labellog.pack()

canvas.create_window(600, 282, anchor=NW, window=frame)
canvas.create_window(600, 100, anchor='nw', window=canvas_iteso_logo)
canvas.mainloop()