positivos = []
negativos = []

for i in range(5):
    numero = int(input(f"Introduce el número {i+1}: "))
    
    if numero >= 0:
        positivos.append(numero)
    else:
        negativos.append(numero)

print("\nNúmeros positivos:", positivos)
print("Suma de positivos:", sum(positivos))
print("\nNúmeros negativos:", negativos)
print("Suma de negativos:", sum(negativos))
