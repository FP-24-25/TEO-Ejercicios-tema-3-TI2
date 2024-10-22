def indice_primera_aparicion(lista, valor):
    '''
    Devuelve la posición de valor en lista.
    Si no existiera valor en lista, devuelve -1.
    '''
    posicion = -1
    for i, elem in enumerate(lista):
        if elem == valor:
            posicion = i
            break
    return posicion

# Probamos la función
lista = ["árbol", "coche", "casa", "peatón"]
print('Posición de "casa":', 
      indice_primera_aparicion(lista, "casa"))
print('Posición de "bicicleta":', 
      indice_primera_aparicion(lista, "bicicleta"))
