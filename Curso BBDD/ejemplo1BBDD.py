import sqlite3

#Abrir Conexión (Lo cual crea la base de datos)
MiConexion=sqlite3.connect("./curso BBDD/PrimeraBase")

#CREAMOS CURSOR O PUNTERO
MiCursor=MiConexion.cursor()

#INSTRUCCION SQL
#MiCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20 ))")
#Visor de SQLite: https://sqlitebrowser.org/dl/

#MiCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'Deportes')")

#Insertar ahora varios registros
""" variosProductos=[
    ("Camiseta", 10, "Deportes"),
    ("Jarrón", 90, "Cerámica"),
    ("Camión", 20, "Juguetería"),            
                ]

MiCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos) """
#Tras cambios en estrucura o contenido

MiCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos2=MiCursor.fetchall()
print(variosProductos2)

for producto in variosProductos2:
    print("Nombre Artículo", producto[0], " Sección", producto[2])


MiConexion.commit()






MiConexion.close()