from tkinter import messagebox
import sqlite3

miConexion=sqlite3.connect("./Q21/Q_Gestion")

miCursor=miConexion.cursor()

mySql="SELECT * FROM SOCIEDADES"
miCursor.execute(mySql)

elUsuario=miCursor.fetchall()

for t in elUsuario:
    messagebox.showinfo("BBDD",t)
""" try:
    miCursor.execute(miSQL)
    messagebox.showinfo("BBDD", "BBDD Creada con éxito.")
except:
    messagebox.showwarning("¡ATENCIÓN!", "La BBDD ya existe") """

miConexion.close()
