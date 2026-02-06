# Juego: Adivina el color secreto
# Explicación del juego:
# El ordenador tiene un color secreto (por ejemplo, "rojo").
# El usuario debe adivinar el color.
# Si el usuario no acierta, el ordenador le dice que lo intente de nuevo.
# El juego continúa hasta que el usuario acierte el color secreto.

# Color secreto (puedes cambiarlo si quieres)


# Inicialización de la variable para adivinar


# Bucle while: continúa hasta que el usuario acierte
    # Pedir al usuario que introduzca un color
    # Dar una pista
color_secreto = "rojo"

color_usuario = ""

while color_usuario != color_secreto:

        color_usuario = input("Adivina el color secreto: ")

        if color_usuario == color_secreto:
            print("¡Correcto! Has adivinado el color secreto.")
        else:
            print("Incorrecto. Intenta de nuevo.")



