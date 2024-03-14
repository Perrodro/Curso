"""LISTAS"""
print("*****LISTAS*****")
miLista=["Pepe","Manolo",48, True] *3 #El operador "*" repite la lista n veces
otraLista=["Margarita","Clara", "Leticia",1025.35,"Concha"]
otraListaMas=["1235", "Jeremías", "Nemesio", "Paco"]

miLista.append("Teresa") #Añade un elemento a la lista (al final)
miLista.insert(2,"Bonifacio") #Inserta un elemento en la lista en el INDEX especificado
miLista.extend(["Julio", "Miguel", "Rodrigo"]) #Extender una lista, al final, con varios elementos
miLista.extend(otraLista)
miLista= miLista + otraListaMas #Unir dos listas con el operador "+"
miLista.remove("Manolo") #Elimina un registro de la Lista
miLista.pop() # Elimina el último registro de una lista

print ("Imprime toda la lista: " , miLista[:]) #Imprime toda la lista
print ("Imprime un elemento buscando desde el final: " , miLista[-1]) #Imprime buscando desde el final. El ultimo elemento será -1
print ("Imprime una porción de lista (desde índice 0 hasta posición 3): " , miLista[0:3]) #Imprime Una Porción de lista
print ("Imprime una porción de lista (nomenclatura abreviada desde índice 0 hasta posición 3): " , miLista[:3]) #Imprime Una Porción de lista (nomenclatura abreviada)
print ("Imprime una porción de lista (nomenclatura abreviada desde índice 2 hasta posición final): " , miLista[2:]) #Imprime Una Porción de lista (nomenclatura abreviada)
print ("Imprime una porción de lista (nomenclatura abreviada): " , miLista[2:]) #Imprime Una Porción de lista (nomenclatura abreviada)
print ("Imprime el índice de un elemento (Leticia): " , miLista.index("Leticia")) #Imprime el índice de un elemento
print ("Imprime True si un elemento (Luis) está en la lista: " , "Luis" in miLista) #Imprime true si un elemento está en la lista
print ("Imprime Talse si un elemento (BMW) está en la lista: " , "BMW" in miLista) #Imprime false si un elemento está en la lista

"""TUPLAS"""
print("*****TUPLAS*****")

miTupla=("Juan",25,1,1971)
miTuplaUnitaria=("Carlos",) #!!!IMPORTANTE la coma tras el elemento unitario

print("Tupla unitaria: ", len(miTuplaUnitaria), " --> ", miTuplaUnitaria)
print(miTupla[:]) #imprime toda la Tupla
print(miTupla[1]) #Acceder a un elemento
miNuevaLista=list(miTupla) #Vuelca la tupla en una lista
miNuevaTupla=tuple(miNuevaLista) #Vuelca la lista en una tupla
print (miNuevaLista[:])
print(miNuevaTupla)
print ("Imprime True si un elemento (Juan) está en la tupla:" , "Juan" in miTupla) #Imprime true si un elemento está en la tupla
print ("Imprime False si un elemento (BMW) está en la tupla:" , "BMW" in miTupla) #Imprime false si un elemento está en la tupla
print ("Devuelve el número de veces que un elemento (Juan) está en la tupla:" , miTupla.count("Juan")) #Imprime el número de veces que un elemento está en la tupla
print ("Devuelve el número de veces elementos de una tupla:" , len(miTupla)) #Devuelve el número de veces elementos de una tupla

nombre, dia, mes, anno =miTupla #Desempaquetado de Tupla. Asignar los elementos de una tupla a variables
print("Desempaquetado de tupla:", nombre, dia, mes, anno)

"""DICCIONARIOS"""
print("*****DICCIONARIOS*****")
miDiccionario={"Alemania":"Berlín","Francia":"Paris","Reino Unido":"Londres", "España":"Madrid"}
miDiccionario["Italia"]="Lisboa" #Añadir un registro al diccionario
miDiccionario["Italia"]="Roma" #Modificar un registro del diccionario
del miDiccionario["Reino Unido"]
print("Acceso al diccionario haciendo referencia a la clave (Francia)",miDiccionario["Francia"])
print("Imprime todo el Diccionario", miDiccionario)
print("Imprime las claves del diccionario", miDiccionario.keys())
print("Imprime los valores del diccionario", miDiccionario.values())
print("Imprime la longitud del diccionario", len(miDiccionario))