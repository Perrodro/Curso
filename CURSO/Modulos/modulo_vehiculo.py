class Vehiculos():

    def __init__(self, marca, modelo):  #Constructor
        
        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self): #Método
        self.enMarcha=True

    def acelerar(self): #Método
        self.acelera=True

    def frenar(self): #Método
        self.frena=True

    def estado(self): #Método
        print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class Furgoneta(Vehiculos):

    def carga(self, cargar):

        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

class moto(Vehiculos): #Clase
    hCaballito=""
    def caballito(self):
        self.hCaballito="Voy haciendo el caballito"
    
    def estado(self): #Método
        print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\nCaballito: ", self.hCaballito)

class VElectricos():
    def __init__(self):
        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True


class BicicletaElectrica(VElectricos,Vehiculos):
    pass
