from collections import namedtuple
Persona = namedtuple("Persona", "nombre, edad")

def lee_personas(n):
    '''
    Lee el nombre y la edad de n personas por teclado, y devuelve
    una lista de tuplas de tipo Persona
    '''
    res = []
    for i in range(1, n + 1):    
        nombre = input(f"Diga el nombre de la persona {i}: ")
        edad = int(input(f"Diga la edad de la persona {i}: "))
        res.append(Persona(nombre, edad))
    return res

'''
Función edad_media, que recibe una lista de personas y devuelva la edad media.
Función mayores_18, que recibe una lista de personas y devuelva una lista ordenada alfabéticamente con los nombres de las personas mayores de edad.
Función edades_distintas, que recibe una lista de personas y devuelva una lista con las edades ordenadas de menor a mayor y sin duplicados.
Función persona_mas_joven, que reciba una lista de personas y devuelva el nombre de la persona de menor edad.
'''

def edad_media(personas):
    suma = 0
    for p in personas:
        suma += p.edad
    
    if len(personas) > 0:
        return suma / len(personas)
    else:
        return None

def mayores_18(personas):
    nombres = []
    for p in personas:
        if p.edad >= 18:
            nombres.append(p.nombre)
    return sorted(nombres)

def edades_distintas(personas):
    edades = set()
    for p in personas:
        edades.add(p.edad)
    return sorted(edades)
    

def persona_mas_joven(personas):
    persona_mas_joven = None
    for p in personas:
        if persona_mas_joven == None or p.edad < persona_mas_joven.edad:
            persona_mas_joven = p

    if persona_mas_joven !=None:
        return persona_mas_joven.nombre
    else:
        return None

personas = lee_personas(3)
print("La edad media es", edad_media(personas))
print("Los nombres de los mayores de 18 son", mayores_18(personas))
print("Las distintas edades son", edades_distintas(personas))
print("La persona más joven es", persona_mas_joven(personas))