# Programa que lee una secuencia de números
# y cuenta cuántos son pares y cuántos impares.
# El programa termina cuando se ingresa un cero.

# Inicializamos los contadores
numeros_senars = 0
numeros_parells = 0

# Leer el primer número
number = int(input("Introduce un número o escribe 0 para detener: "))

# Mientras el número no sea cero, seguimos leyendo
while number != 0:
    # Verificar si el número es impar
    if number % 2 == 1:
        numeros_senars += 1  # Incrementar contador de impares
    else:
        numeros_parells += 1  # Incrementar contador de pares
    
    # Leer el siguiente número
    number = int(input("Introduce un número o escribe 0 para detener: "))

# Mostrar resultados
print("Cantidad de números pares:", numeros_parells)
print("Cantidad de números impares:", numeros_senars)
