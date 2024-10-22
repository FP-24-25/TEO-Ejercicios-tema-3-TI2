def calcula_precios(precio_normal, edades):
    '''
    Recibe el precio normal de la entrada,
    y una lista con edades, y devuelve una lista
    con el precio que le corresponde a cada persona
    (si tienen 18 o menos o 65 o más, pagan el 50%)
    '''
    precio_reducido = precio_normal / 2
    precios = []
    for edad in edades:
        if edad <= 18 or edad >= 65:
            precios.append(precio_reducido)
        else:
            precios.append(precio_normal)
    return precios

# Probamos la función
precios = calcula_precios(6, [8, 18, 24, 44, 64, 65, 70])
print(precios)