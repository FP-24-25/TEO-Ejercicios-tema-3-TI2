def fecha_en_intervalo(fecha, fecha_min, fecha_max):
    return (fecha_min == None or fecha_min <= fecha)\
            and (fecha_max == None or fecha <= fecha_max)