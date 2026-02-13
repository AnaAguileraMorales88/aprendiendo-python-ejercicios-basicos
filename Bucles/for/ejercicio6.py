# La teva tasca aquí és molt especial: Has de dissenyar un
# devorador de vocals!
# Escriu un programa que utilitzis:
# un bucle for;
# el concepte d'execució condicional ( if-elif-else ).
# La sentència continuar.
# El teu programa deu ser capaç:
# demanar a l'usuari que ingressi una paraula.
# utilizarpalabra_usuari = paraula_usuari.upper()per a convertir la paraula ingressada per l'usuari a majúscules; p
# arlarem sobre els anomenats mètodes de cadena i el métodosuperior() Molt aviat, no et preocupis
# utilitzi l'execució condicional i la instrucció continuar per a "devorar" les vocals A , I , I , O , O de la paraula
# ingressada.
# Imprimeix les lletres no consumides en la pantalla, cadascuna d'elles en una línia separada.
# Si la lletra no és una vocal

# Demanem a l'usuari que introdueixi una paraula
palabra_usuario = input("Introduce una palabra: ")

# Convertim la paraula a majúscules
palabra_usuario = palabra_usuario.upper()

# Definim les vocals
vocales = "AEIOU"

# Filtrar i imprimir només les consonants
for letra in palabra_usuario:

    if letra in vocales:
        continue
    print(letra)

