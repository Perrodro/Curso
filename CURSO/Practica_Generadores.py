print("Práctica Generadores: Función estandar")
def generaPares(limite):

    num=1

    miLista=[]

    while num<limite:

        miLista.append(num*2)

        num=num+1
    
    return miLista

print (generaPares(10))

print("Práctica Generadores: Generador")

def generaParesGen(limite):

    num=1

    while num<limite:

        yield num*2

        num=num+1
devuelvePares=generaParesGen(10)

""" for i in devuelvePares:

    print(i)
 """
print(next(devuelvePares))

print("Aquí podría ir más código")

print(next(devuelvePares))

print("Aquí podría ir más código")

print(next(devuelvePares))

print("Practica Generadores: YIELD FROM")

def devuelveCiudades(*ciudades): #El asterisco signauifica que va a recibir un número indeterminado de elementos en forma de TUPLA
    for elemento in ciudades:
        #for subElemento in elemento: #En lugar de este bucle anidado
            yield from elemento # en lugar de 'yield subElemento'

ciudadesDevueltas=devuelveCiudades("Madrid","Barcelona","Bilbao", "Valencia")

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))