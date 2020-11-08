#Gabriel Olvera Luis Fernando Casas
from tkinter import *
import tkinter




import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://iteso-parking.firebaseio.com/'
})
window = tkinter.Tk()
canvas = Canvas(window, width = 1980, height = 1020)
canvas.pack()
ref = db.reference('/')
et_1 = tkinter.Label(window, text= "tytpe in the state of Cajon 135")
input_state = tkinter.StringVar()
input_entry = tkinter.Entry(window, textvariable=input_state)
et_1.pack()
input_entry.pack()
et_2 = tkinter.Label(window, text= "tytpe in the state of Cajon 120")
et_2.pack()
input_state2 = tkinter.StringVar()
input_entry2 = tkinter.Entry(window, textvariable=input_state2)
input_entry2.pack()
img = PhotoImage(file='arboles.ppm')
canvas.create_image(20,20, anchor=NW, image=img)
def updateReference():
    state1 = input_state.get()
    print(state1)
    state_2 = input_state2.get()
    print(state_2)
    ref.set({
        ' Ejemplo':
            {
                'Cajon 135':{
                    'number':'135',
                    'State' : state1 ,
                    'ID' : '135Z2B'

                },
            'Cajon 120': {
                   'number' : '120',
                'State' : state_2,
                'ID' : '120Z2B'


                }
            }

    })
Ref_button = tkinter.Button(window, text="Update Reference", command = updateReference())
Ref_button.pack()
window.mainloop()
'''
#Update data

#Primeros creamos una referencia de la base de datos
rref = db.reference('Ejemplo') #En este caso pongo ejemplo por que quiero modificar el child o el atributo de este objeto
cajon_ref= rref.child('Cajon') #Nombre del child

cajon_ref.update({
    'number': '666'
})

#Modificar Muchos

rrref =db.reference('Cajon')
rrref .update({
    'Arthut/number': '619',
    'Cajon/number' : '765'
})

#How to get the data from the REALTime Database
reref= db.reference('Cajon')
num_ref = reref.child('Cajon')
nnum_ref = num_ref.child('number')

'''