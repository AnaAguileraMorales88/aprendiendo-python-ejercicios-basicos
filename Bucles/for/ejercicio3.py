numero = int(input("Introduce un número entero positivo: "))

suma_total = 0
pares = []

print(f"\nTabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    suma_total += resultado
    
    if resultado % 2 == 0:
        pares.append(resultado)

print("\nSuma de todos los resultados:", suma_total)
print("Resultados pares:", pares)
