from io import open

#ABRIR EL ARCHIVO EN MODO ESCRITURA
archivo_texto=open("archivo.txt", "w")

frase="Estupendo día para estudiar Python \nel miercoles"

archivo_texto.write(frase)

archivo_texto.close() 

#ABRIR EL ARCHIVO EN MODO LECTURA
archivo_texto=open("archivo.txt", "r")

#texto=archivo_texto.read()
print(archivo_texto.read(9))
archivo_texto.seek(5)
print(archivo_texto.read())

archivo_texto.close()

#print(texto)

#ABRIR EL ARCHIVO EN MODO APPEND
archivo_texto=open("archivo.txt", "a")

archivo_texto.write("\nSiempre es una buena ocasion para estudiar Python")

archivo_texto.close()