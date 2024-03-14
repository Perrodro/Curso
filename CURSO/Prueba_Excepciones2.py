def divide():

    try:

        op1=float(input("Introduce el primer número (numerador): "))
        op2=float(input("Introduce el segundo número (denominador): "))

        print("La división es: " + str(op1/op2))
    except ValueError:
        print("El valor introducido no es correcto.")
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
    finally:
        print("Cálculo finalizado")

divide()