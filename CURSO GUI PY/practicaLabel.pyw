from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)
miFrame.pack()

miImagen=PhotoImage(file="T.png")

#miLabel= Label(root,text="Hola Python")
#miLabel.place(x=100,y=200)

#Label(root, text="Hola Python",fg="Red", font=("Speak Pro",18)).place(x=100,y=200) #Nomenclaura Abreviada
Label(root, image=miImagen).place(x=100,y=200) #Nomenclaura Abreviada

root.mainloop()