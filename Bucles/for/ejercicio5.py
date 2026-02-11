filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))

matriz = []
suma_total = 0
numero_mayor = None

for i in range(filas):
    fila = []
    print(f"\nFila {i+1}")
    
    for j in range(columnas):
        numero = int(input(f"Introduce el valor para posición [{i}][{j}]: "))
        fila.append(numero)
        suma_total += numero
        
        if numero_mayor is None or numero > numero_mayor:
            numero_mayor = numero
    
    matriz.append(fila)

# Mostrar matriz
print("\n--- MATRIZ ---")
for fila in matriz:
    print(fila)

# Suma por filas
print("\n--- Suma por filas ---")
for i in range(len(matriz)):
    print(f"Fila {i+1}: {sum(matriz[i])}")

print("\nSuma total de la matriz:", suma_total)
print("Número mayor de la matriz:", numero_mayor)
