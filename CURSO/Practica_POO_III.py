#CONSTRUIR UNA CLASE.
class Coche():  # Nombre con la inicial en Mayúscula
    def __init__(self):  #Método Constructor de estado Incial
        self.__largoChasis=250  #Propiedades iniciales de la clase
        self.__anchoChasis=120  #Propiedades iniciales de la clase
        self.__ruedas=4         #Propiedades iniciales de la clase
        self.__enMarcha=False   #Propiedades iniciales de la clase

    def arrancar(self,arrancamos):  #CREAR UN METODO def arrancar(self): --> self hace referencia al propio objeto (o instancia) perteneciente a la clase
        # pass -> porque el metodo está vacio
        self.__enMarcha=arrancamos

        if(self.__enMarcha):
            chequeo=self.__chequeoInterno()

        if(self.__enMarcha and chequeo):  #No hace falta poner "=True"
            return "El coche está en marcha"
        elif(self.__enMarcha and chequeo==False):
            return("Algo ha ido mal en el chequeo")
        else:
            return "El coche está parado"
    
        #self.enMarcha=True #cuando acceda desde miCoche esta expresión= miCoche.enMarcha=true




    def estado(self):
        print("El coche tiene", self.__ruedas,"ruedas. Un ancho de", self.__anchoChasis,"y un largo de", self.__largoChasis)

    def __chequeoInterno(self):
        print("Realizando Chequeo Interno.")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas":
            return True
        else:
            return False

#CONSTRUIR UN OBJETO
miCoche=Coche() #Esto es "instanciar una clase"


print(miCoche.arrancar(True))
miCoche.estado()
#print(miCoche.__chequeoInterno()) #Quitamos estas llamadas porque ya no es accesible el Método (lo he encapsulado)

print("*************** A continuación, creamos el siguinete Objeto ***************")

miCoche2=Coche()

print(miCoche2.arrancar(False))
miCoche2.estado()

#print(miCoche2.__chequeoInterno()) #Quitamos estas llamadas porque ya no es accesible el Método (lo he encapsulado)