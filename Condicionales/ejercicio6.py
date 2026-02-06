try:
    numero = int(input("Introduce un número entero: "))
    
    if numero > 0:
        print("El número es positivo")
    elif numero < 0:
        print("El número es negativo")
    else:
        print("El número es cero")
except ValueError:
    print("Error: debes introducir un número entero válido")
