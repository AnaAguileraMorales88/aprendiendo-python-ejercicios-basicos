# Escenari:
# Escriu un programa que determini si un número és:
# Parell: Si el número és divisible entre 2.
# Senar: Si el número no és divisible entre 2.
# Especial: Si el número és divisible entre 2 i també és divisible entre 5.
# El programa ha de:
# Acceptar un número enter com a entrada.
# Mostrar un missatge segons les regles anteriors.
# Si el número és negatiu, mostrar un advertiment: "El número ha de ser positiu."
# Demanem un número a l'usuari

numero = int(input("Introduce un número: "))
if numero < 0:
    print("El numero tiene que ser positivo")
else:  

    if numero % 2 == 0 and numero % 5 == 0:
        print("especial")
    elif numero % 2 == 0:
        print("Parell")
    else:
        print("senar")


