"""IF"""
print("IF")

notaAlunmo=int(input("Introduce la nota del Alumno: "))

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion

print(evaluacion(notaAlunmo))