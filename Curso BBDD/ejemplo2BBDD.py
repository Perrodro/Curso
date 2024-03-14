import sqlite3

miConexion=sqlite3.connect("./Curso BBDD/GestionProductos")

miCursor=miConexion.cursor()

miCursor.execute('''
                 CREATE TABLE PRODUCTOS (
                 ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 NOMBRE_ARTICULO VARCHAR (50) UNIQUE,
                 PRECIO INTEGER,
                 SECCION VARCHAR(20))
                 ''')

productos=[

    ("Pelota", 20, "Juguetería"),
    ("Pantalón", 15, "Confección"),
    ("Destornillador", 25, "Ferretería"),
    ("Jarrón", 45, "Cerámica"),
    ("Pantalones", 35, "Confección")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)
#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05','Tren',15,'Jugetería')")


miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='Pelota'")

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Confección'")

productosLeer=miCursor.fetchall()

print (productosLeer)


miConexion.commit()

miConexion.close()    