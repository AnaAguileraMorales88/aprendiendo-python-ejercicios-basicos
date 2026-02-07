numero = int(input("Introduce un número entero positivo: "))

if numero <= 1:
    print("No es un número primo")
else:
    es_primo = True

    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            print(f"No es primo, es divisible entre {i}")
            break  # Aquí salimos en cuanto encontramos un divisor

    if es_primo:
        print("Es un número primo")
