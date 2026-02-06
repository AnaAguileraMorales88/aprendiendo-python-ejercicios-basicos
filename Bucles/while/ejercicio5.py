# Explicación del juego:
# El ordenador elige un número secreto (por ejemplo, un número entre 1 y 10).
# El usuario debe adivinar el número.
# Si el usuario no acierta, el ordenador le da una pista (por ejemplo, "Más alto" o "Más bajo").
# El juego continúa hasta que el usuario acierte el número secreto.

# Número secreto (puedes cambiarlo si quieres)


# Inicialización de la variable para adivinar


# Bucle while: continúa hasta que el usuario acierte

    # Pedir al usuario que introduzca un número

    # Dar una pista

numero_secreto = 6

numero_usuario = 0

while numero_usuario != numero_secreto:
    
        numero_usuario = int(input("Adivina el número secreto: "))

        if numero_usuario < numero_secreto:
            print("Es más alto")

        elif numero_usuario > numero_secreto:
            print("Es mas bajo")

        else:
            print("Has acertado")
