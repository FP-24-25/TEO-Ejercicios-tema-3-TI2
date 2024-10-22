def imprime_pares_inverso(n):
    '''
    Imprime los números positivos pares menores 
    o iguales a n, en orden inverso
    '''
    if n%2 == 0:
        numero = n
    else:
        numero = n-1
    while numero >= 2:
        print(numero, end=" ")
        numero -= 2
    # Ahora con range
    # TODO

# Probamos la función
imprime_pares_inverso(10)