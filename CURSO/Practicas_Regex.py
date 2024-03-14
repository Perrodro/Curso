import re

""" cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

textoBuscar="Python"

if re.search(textoBuscar,cadena) is not None:
    print ("He encontrado el texto")
else:
    print("No he encontrado el texto")

textoEncontrado=re.search(textoBuscar,cadena)

print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span())

print(len(re.findall(textoBuscar, cadena)))

#-----ANCLAS y CLASES DE CARACTERES-----
lista_nombres=['Ana Gómez', 
               'María Martín', 
               'Sandra López', 
               'Santiago Martín',
               'Sandra Fernández',
               'Ernesto Niño',
               'Carlos Niña',
               'Ana Gomez']

for elemento in lista_nombres:
    if re.findall('^Sandra', elemento):
        print(elemento)
    if re.findall('Martín$', elemento):
        print(elemento)
    if re.findall('Niñ[oa]', elemento):
        print(elemento)
    if re.findall('G[oó]mez', elemento):
        print(elemento) """

#----RANGOS----
        
""" lista_nombres=['Ana1', 
               'Pedro', 
               'María', 
               'Rosa',
               'Sandra',
               'Delia',
               'Carlos',
               'Jeremías',
               'Ana2',
               'Ana3',
               'Ana4',
               'AnaA',
               'AnaB',
               'AnaC']

for elemento in lista_nombres:
    if re.findall('^[O-T]', elemento):
        print("1.-", elemento)
for elemento in lista_nombres:
    if re.findall('[o-t]$', elemento):
        print("2.-", elemento)
for elemento in lista_nombres:
    if re.findall('Ana[0-2]$', elemento):
        print("3.-", elemento)
for elemento in lista_nombres:
    if re.findall('Ana[^0-2]$', elemento):
        print("4.-", elemento)
for elemento in lista_nombres:
    if re.findall('Ana[0-2A-B]$', elemento):
        print("5.-", elemento) """

#----MATCH----
        
nombre1="Sandra López"
nombre2="Antonio Gómez"
nombre3="María López"

if re.match("sandra", nombre1, re.IGNORECASE):
    print("He encontrado el Nombre")
else:
    print("No lo he enecontado")

if re.match(".aría", nombre3, re.IGNORECASE):
    print("He encontrado el Nombre")
else:
    print("No lo he enecontado")

if re.search("López", nombre2, re.IGNORECASE):
    print("He encontrado el Nombre")
else:
    print("No lo he enecontado")