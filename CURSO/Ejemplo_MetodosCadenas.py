NombreUsuario=input("Introduce tu nombre de usuario: ")

print("El nombre es:", NombreUsuario)
print("El nombre en mayusculas es:", NombreUsuario.upper())
print("El nombre en minusculas es:", NombreUsuario.lower())
print("El nombre en Inicial es:", NombreUsuario.capitalize())


edad=input("Introduce la edad: ")

while not(edad.isdigit()):
    print("Por favor introduce un valor numérico.")
    edad=input("Introduce la edad: ")

if (int(edad)<18):
    print("No puede pasar")
else:
    print("Puedes pasar")