from tkinter import *
import tkinter as tk
import pyrebase

config = {
  "apiKey": "AIzaSyA1ijWIJ8vBWiDNm7AV4ZC1Dk4UpHQUvqs",
  "authDomain": "iteso-parking.firebaseapp.com",
  "databaseURL": "https://iteso-parking.firebaseio.com",
  "storageBucket": "iteso-parking.appspot.com",
  "serviceAccount": "D:\Archivos  ITESO\Clases\Algoritmos y Programacion\ITESO Parking\ITESOparking\juan.json"
}
firebase = pyrebase.initialize_app(config)
active_user = ''
db = firebase.database()
all_users = db.child("Usuarios").get()


condicion = False

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
#Registro
arrayusuarios = []
for user in all_users.each():
    arrayusuarios.append(str(user.key()))

#Funcion que valida usuarios para registrar
def validuser():
    user = userio.get()
    correcto = False

    while correcto == False:
        if user in arrayusuarios:
            label["text"] = "El usuario ya existe"

            break
        if len(user) == 0:
            label["text"] = "El usuario no puede estar vacio"

            break
        if user.isalnum() == True:
            label["text"] = "El usuario debe contener algun caracter especial"


            break
        if len(user) > 20:
            label["text"] = "El usuario no puede tener mas de 20 caracteres"

            break
        if len(user) < 20 and user.isalnum() == False and len(user)> 0:
            return True
            label["text"] = ""
            break


#Funcion que valida la contraseña para registrar
def validcontra():
    contra = password.get()
    correcto = False

    while correcto == False:
        if len(contra) < 8:
            label["text"] = "La contraseña debe ser mayor a 8 caracteres"

            break

        if contra.isalnum() == True:
            label["text"] = "La contraseña debe contener algun caracter especial"

            break

        if contra.isupper() == True or contra.islower() == True:
            label["text"] = "La contraseña debe contener mayusculas y minusculas"

            break

        if contra.count(" ") > 0:
            label["text"] = "La contraseña no debe llevar espacios"

            break

        if len(contra) > 8 and contra.isalnum() == False and contra.isupper() == False and contra.islower() == False and contra.count(" ") == 0 and validuser()==True:
            correcto = True
            label["text"] = "Valido"
            return True
            break


#funcion para el boton que valida las credenciales del registro
def validbutton():
    button["state"] = DISABLED
    if validuser() == True and validcontra() == True:
        button["state"] = ACTIVE

#Funcion para la entrada de texto
def entry(txt):
    l=tk.Label(frame,text=txt,width=32)
    l.pack()
    e = tk.Entry(frame,text=txt,width=32, textvariable=userio)
    e.pack()

#Funcion para registrar en la base de datos las credenciales
def register():
    print("Se registro")
    usr = userio.get()
    pswrd = password.get()
    json = {
        usr: {'password': pswrd}
    }
    db.child("Usuarios").update(json)





userio = tk.StringVar()
user = entry("Username")



j = tk.Label(frame,text = "Password",width=32).pack()
password = tk.StringVar()
e=tk.Entry(frame,show="*",text = "Password",width=32, textvariable = password).pack()



button =tk.Button(frame, state=DISABLED,text="Registrar", command = register)
button.pack()

buttovalid = tk.Button(frame,text="Validar",command = validbutton)
buttovalid.pack()

label = Label(frame)
label.pack()


canvas.create_window(600, 282, anchor=NW, window=frame)
canvas.create_window(600, 100, anchor='nw', window=canvas_iteso_logo)
canvas.mainloop()
