from tkinter import *

raiz=Tk()

raiz.title("Ventana de Pruebas")
#raiz.resizable(1,1) #Ancho, alto. Tambien podemos usar True y False
raiz.iconbitmap("T.ico")
#raiz.geometry("650x300") #Tamaño Ventana. La ventana siempre se ajusta al tamaño de su frame
raiz.config(bg="green")

miFrame=Frame() #Instanciamos una variable de CLASE frame
#miFrame.pack(side="bottom", anchor="w") #Empaquetamos el frame DENTRO de la raiz. Anchor tiene nomenclatura North, south, east, west
miFrame.pack(fill="x", expand=True) #Fill usa nomenclatura deejes de coordenadas X, Y, both o none
miFrame.config(bg="Red")
miFrame.config(width=650,height=350)
miFrame.config(bd=5)
miFrame.config(relief="raised")
miFrame.config(cursor="hand2")

raiz.mainloop()