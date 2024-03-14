from tkinter import *
from tkinter import messagebox
import sqlite3

#-----FUNCIONES-----
def ConexionBBDD():
    miConexion=sqlite3.connect("./PRACTICA_GUIADA/Usuarios")

    miCursor=miConexion.cursor()

    try:
        miCursor.execute('''
                        CREATE TABLE DATOSUSUARIOS (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NOMBRE_USUARIO VARCHAR(50),
                        PASSWORD VARCHAR(50),
                        APELLIDO VARCHAR(10),
                        DIRECCION VARCHAR(50),
                        COMENTARIOS VARCHAR(100))
                        ''')
        messagebox.showinfo("BBDD", "BBDD Creada con éxito.")
    except:
        messagebox.showwarning("¡ATENCIÓN!", "La BBDD ya existe")

def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicaión?")

    if valor=="yes":
        root.destroy()

def limpiarCampos():
    miId.set("")
    miNombre.set("")
    miApellido.set("")
    miPass.set("")
    miDireccion.set("")
    textoComentario.delete(1.0,END)

def crear():
    miConexion=sqlite3.connect("./PRACTICA_GUIADA/Usuarios")

    miCursor=miConexion.cursor()
    #Ver consultas parametrizadas: vides 47 a 53 curso PHP/MySQL
    
    datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(), textoComentario.get(1.0,END)
    
    miCursor.execute ("INSERT INTO DATOSUSUARIOS VALUES (NULL,?,?,?,?,?)", (datos))
    """     miCursor.execute ("INSERT INTO DATOSUSUARIOS VALUES (NULL, '" + miNombre.get() + 
                      "','" + miPass.get() + 
                      "','" + miApellido.get() + 
                      "','" + miDireccion.get() + 
                      "','" + textoComentario.get(1.0,END) + "')") """
    
    miConexion.commit()
 
    messagebox.showinfo("BBDD", "Registro insertado con éxito")

def leer():
    miConexion=sqlite3.connect("./PRACTICA_GUIADA/Usuarios")

    miCursor=miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miId.get())

    elUsuario=miCursor.fetchall()

    for usuario in elUsuario:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        textoComentario.insert(1.0, usuario[5])

    miConexion.commit()

def actualizar():
    miConexion=sqlite3.connect("./PRACTICA_GUIADA/Usuarios")

    miCursor=miConexion.cursor()
    #Ver consultas parametrizadas: vides 47 a 53 curso PHP/MySQL

    datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(), textoComentario.get(1.0,END)

    """ miCursor.execute ("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() + 
                      "', PASSWORD='" + miPass.get() + 
                      "', APELLIDO='" + miApellido.get() + 
                      "', DIRECCION='" + miDireccion.get() + 
                      "', COMENTARIOS='" + textoComentario.get(1.0,END) + 
                      "' WHERE ID=" + miId.get()) """
    
    miCursor.execute ("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=? " +
                    "WHERE ID=" + miId.get(),(datos))

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro Actualizado con éxito")

def eliminar():
    miConexion=sqlite3.connect("./PRACTICA_GUIADA/Usuarios")

    miCursor=miConexion.cursor()

    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miId.get())

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro eliminado con éxito")  


root=Tk()

#-----BARRA MENÚ-----
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=ConexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear",command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#----COMIENZO DE CAMPOS----
miFrame=Frame(root)
miFrame.config(bg="dodger blue")
miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miFrame,bg = "snow2", textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame,bg = "snow2", textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="left")

cuadroPass=Entry(miFrame,bg = "snow2", textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame,bg = "snow2", textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame,bg = "snow2", textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario=Text(miFrame,bg = "snow2", width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
ScrollVert=Scrollbar(miFrame, command=textoComentario.yview)
ScrollVert.grid(row=5,column=2, sticky="nsew")

textoComentario.config(yscrollcommand=ScrollVert.set,bg = "snow2")

#-----COMIENZAN LOS LABEL-----
idLabel=Label(miFrame,fg = "white", bg = "dodger blue", text="Id:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame,fg = "white", bg = "dodger blue",text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame,fg = "white", bg = "dodger blue",text="password:")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame,fg = "white", bg = "dodger blue",text="Apellido:")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame,fg = "white", bg = "dodger blue",text="Dirección:")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame,fg = "white", bg = "dodger blue",text="Comentarios:")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#-----BOTONES-----
miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2,text="Crear", command=crear)
botonCrear.grid(row=1,column=0,sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2,text="Leer", command=leer)
botonLeer.grid(row=1,column=1,sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2,text="Actualizar", command=actualizar)
botonActualizar.grid(row=1,column=2,sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2,text="Borrar", command=eliminar)
botonBorrar.grid(row=1,column=3,sticky="e", padx=10, pady=10)

root.mainloop()