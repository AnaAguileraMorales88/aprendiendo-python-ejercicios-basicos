major_numero = -99999999  # Inicialitzem el número més gran amb un valor molt petit
comptador = 0  # Inicialitzem el comptador de números introduïts

# Demanem el primer número
numero = int(input("Introdueix un número o escriu -1 per finalitzar el programa: "))

while numero != -1:  # Mentre el número no sigui -1, continuem
    # Si el número és negatiu (però no -1), saltem aquesta iteració amb continue
    if numero < 0:
        print("Els números negatius no es tenen en compte. Introdueix un altre número.")
        numero = int(input("Introdueix un número o escriu -1 per finalitzar el programa: "))
        continue  # Saltem a la següent iteració del bucle
    
    comptador += 1  # Incrementem el comptador de números introduïts
    
    if numero > major_numero:  # Si el número introduït és més gran que el més gran registrat
        major_numero = numero  # Actualitzem el número més gran
    
    # Demanem el següent número
    numero = int(input("Introdueix un número o escriu -1 per finalitzar el programa: "))

# Després del bucle, comprovem si s'han introduït números
if comptador > 0:  # Si s'han introduït números
    print("El número més gran introduït és:", major_numero )
else:  # Si no s'han introduït números
    print("No s'han introduït números vàlids.")