from Modulos import funciones_matematicas
class Areas:
    """Esta clase calcula las areas de diferentes figuras geométricas"""

    def areaCuadrado(lado):
        """Calcula el area de un cuadrado
            elevando al cuadrado el lado pasado por parámetro"""
        return ("El area del cuadrado es: " + str(lado*lado))
    def areaTrianguno(base, altura):
        """Calcula el area de un triangula multiplicando la base pasada por parámetro y la altura pasada por parametro, diviviendo por 2"""
        return ("El area del triángulo es: " + str(base*altura/2))

#print(areaCuadrado(2))
#print(areaCuadrado.__doc__)
help(Areas.areaTrianguno)
help(Areas)
help (funciones_matematicas)
