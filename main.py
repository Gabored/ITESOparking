#Gabriel Olvera Luis Fernando Casas
import tkinter

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://iteso-parking.firebaseio.com/'
})
window = tkinter.Tk()
window.geometry("1600x1000")
ref = db.reference('/')
et_1 = tkinter.Label(window, text= "tytpe in the state of Cajon 135")
input_state = tkinter.Entry(window)
et_1.pack()
input_state.pack()
et_2 = tkinter.Label(window, text= "tytpe in the state of Cajon 120")
et_2.pack()
input_state2 = tkinter.Entry(window)
input_state2.pack()

def updateReference():
    state1 = str(input_state.get())
    print(state1)
    print("Ho")
    state_2 = str(input_state2.get())
    print(state_2)
    ref.set({
        ' Ejemplo':
            {
                'Cajon 135':{
                    'number':'135',
                    'State' : 'Hahaha' ,
                    'ID' : '135Z2B'

                },
            'Cajon 120': {
                   'number' : '120',
                'State' : 'Free',
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