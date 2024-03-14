class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} €.".format(self.nombre, self.cargo, self.salario)
    
lista_empleados=[
    Empleado("Juan", "Director", 6700),
    Empleado("Ana", "Administrativo", 2500),
    Empleado("Roberto", "Presidente", 15000),
    Empleado("Paco", "Conserje", 1100),
    Empleado("Sara", "Secretaria", 1400)
]

def calculo_comision(empleado):
    
    if empleado.salario<=3000:

        empleado.salario=empleado.salario*1.03

    return empleado

listaEmpleadosComision=map(calculo_comision, lista_empleados)

for empleado in listaEmpleadosComision:
    print(empleado)