# Escenario:
# Escribe un programa que determine si un número es:
# Par: Si el número es divisible entre 2.
# Impar: Si el número no es divisible entre 2.
# Especial: Si el número es divisible entre 2 y también es divisible entre 5.
# El programa debe:
# Aceptar un número entero como entrada.
# Mostrar un mensaje según las reglas anteriores.
# Si el número es negativo, mostrar una advertencia: "El número debe ser positivo."
# Pedir un número al usuario.


numero = int(input("Introduce un número: "))
if numero < 0:
    print("El numero debe ser positivo")
else:
    if numero % 2 == 0 and numero % 5 == 0:
        print("Especial")
    elif numero % 2 == 0:
        print("Par")
    else:
        print("Impar")


