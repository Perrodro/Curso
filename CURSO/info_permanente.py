import pickle

class Persona:
    def __init__(self,nombre,genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Seha creado una persona nueva con el nombre de",self.nombre)
              
    def __str__(self): # MÉTODO especial que convierte en cadena de texto la información de un OBJETO
        return "{} {} {}".format(self.nombre, self.genero, self.edad) #Nomenclatura para formato

class ListaPersonas: # CLASE para guardar lista
    personas=[]

    def __init__(self):
        listaDePersonas=open("ficheroExterno", "ab+")
        listaDePersonas.seek(0) #Desplazar el cursor a la posición 0 del archivo

        try:
            self.personas=pickle.load(listaDePersonas) #Volcado de información en el fichero
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero está vacío")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, p): #MÉTODO para agregar personas a la lista
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self): # MÉTODO para mostrar personas de la lista
        for p in self.personas:
            print (p)

    def guardarPersonasEnFicheroExterno(self): #MÉTODO para guardar en el fichero la lista
        ListaDePersonas=open("FicheroExterno","wb")
        pickle.dump(self.personas, ListaDePersonas) #Volcado de información en el fichero
        ListaDePersonas.close()
        del (ListaDePersonas)

    def mostrarInfoFicheroExterno(self): #MÉTODO para mostrar la información del fichero
        print("La información del fichero externo es la siguiente: ")
        for p in self.personas:
            print (p)

miLista=ListaPersonas() # OBJETO de tipo ListaPersonas. INSTANCIAR objeto

p=Persona("Sandra","Femenino", 29) #Objeto "p" de la CLASE persona
miLista.agregarPersonas(p) #Agregamos la persona a la lista
p=Persona("Manolo","Masculino", 49)
miLista.agregarPersonas(p)
p=Persona("Carlota","Femenino", 55)
miLista.agregarPersonas(p)

miLista.mostrarPersonas() #Llamamos a ese MÉTODO para que nos muestre la información almacenada en la lista
miLista.mostrarInfoFicheroExterno()