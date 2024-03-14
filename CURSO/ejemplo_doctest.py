def areaTriangulo(base, altura):
    """
    Calcula el area de un triangula multiplicando la base pasada por parámetro y la altura pasada por parametro, diviviendo por 2
    >>> areaTriangulo(3,6)
    9.0
    
    
    """
    return (base*altura/2) 

import doctest
doctest.testmod()


def compruebaMail(mailUsuario):
    """
    la función comprueba que el email recibido por parámetro tiene @
    Si tiene una arroba es correcto.
    Si tieme más de una es incorrecto.
    Si la @ esta al final es incorrecto

    >>> compruebaMail('correo@correcto.es')
    True
    >>> compruebaMail('correocorrecto.es@')
    False
    >>> compruebaMail('correocorrecto.es')
    False
    >>> compruebaMail('correo@@correcto.es')
    False
    
    """

    arroba=mailUsuario.count('@')
    if arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0:
        return False
    else:
        return True 

doctest.testmod()