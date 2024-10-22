import random

def juego_adivina_numero(maximo):
    # Paso 1: "pensar" el número
    numero_secreto = random.randint(1, maximo)    
    while True:
        # Paso 2: pedirle un número al jugador
        numero = int(input(f"Di un número entre 1 y {maximo}:"))        
        # Paso 3: 
        # Si el número es correcto, FIN
        if numero_secreto == numero:
            print("¡Has acertado!")
            break
        # Si el número introducido es menor o mayor, 
        # informar al jugador, e ir al Paso 2
        elif numero_secreto > numero:
            print("El número que he pensado es mayor")
        else:
            print("El número que he pensado es menor")
