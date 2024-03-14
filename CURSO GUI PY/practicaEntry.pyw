from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

miNombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(column=1,row=0,padx=10,pady=10)
cuadroNombre.config(fg="red", justify="right")

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(column=0,row=0, sticky="w",padx=10,pady=10)

cuadroPass=Entry(miFrame)
cuadroPass.grid(column=1,row=1,padx=10,pady=10)
cuadroPass.config(fg="yellow", bg="black",show="*")

PassLabel=Label(miFrame, text="Password: ")
PassLabel.grid(column=0,row=1, sticky="w",padx=10,pady=10)

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(column=1,row=2,padx=10,pady=10)

ApellidoLabel=Label(miFrame, text="Apellido 1: ")
ApellidoLabel.grid(column=0,row=2, sticky="w",padx=10,pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(column=1,row=3,padx=10,pady=10)

DireccionLabel=Label(miFrame, text="Dirección: ")
DireccionLabel.grid(column=0,row=3, sticky="w",padx=10,pady=10)

cuadroComentario=Text(miFrame, width=16, height=5)
cuadroComentario.grid(column=1,row=4,padx=10,pady=10)

scrollComentario=Scrollbar(miFrame, command=cuadroComentario.yview)
scrollComentario.grid(row=4,column=2, sticky="nsew")

cuadroComentario.config(yscrollcommand=scrollComentario.set)

ComentarioLabel=Label(miFrame, text="Comentario: ")
ComentarioLabel.grid(column=0,row=4, sticky="w",padx=10,pady=10)

def codigoBoton():
    miNombre.set("Roberto")

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()

raiz.mainloop() 