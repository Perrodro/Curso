import pickle

lista_nombres=["Pedro", "Ana", "María", "Isabel"]

fichero_binario=open("lista nombres", "wb") # wb.- Escritura binaria

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del fichero_binario #Para borrar el fichero de la memoria

fichero_binario=open("lista nombres", "rb") #rb.- Lectura binario

lista=pickle.load(fichero_binario)

print(lista)