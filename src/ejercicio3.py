def imprime_pares(n):
    '''
    Imprime los números positivos pares menores 
    o iguales a n
    '''
    # numero = 2
    # while numero <= n:
    #     print(numero, end=" ")
    #     numero += 2
    # Ahora con range
    for numero in range(2, n+1, 2):
        print(numero, end=" ")

# Probamos la función
imprime_pares(10)