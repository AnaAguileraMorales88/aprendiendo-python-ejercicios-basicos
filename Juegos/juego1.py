suma = 0
contador = 0

while True:
    numero = int(input("Introduce un número (0 para terminar): "))
    
    if numero == 0:
        break
    
    suma += numero
    contador += 1

print("Has introducido", contador, "números")
print("La suma total es:", suma)
