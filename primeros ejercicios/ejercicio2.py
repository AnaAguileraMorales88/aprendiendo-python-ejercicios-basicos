
"""Escenari
Modifica la primera línia de codi en l'editor, usant les paraules claus reservades sep i end,, perquè s'obtingui la sortida esperada. Empra dos funcio print() en l'editor.
No canviïs res en la segona invocació de print().
Sortida Esperada"""
#Programming****Essentials****in...Python

print("Programmin","Essentials", "in", sep=" **** ", end=" ... ")
print("Python")

for letra in word:
    print(letra, end="*")

print("A\nN\nA") #\n salta a una nueva línea

print("Dime lo que sea...")
caixa = input()
print("mmm...", caixa, "...¿en serio?")

anything = input("Dime lo que sea...")
print("mmmm...", anything, "...¿en serio?")

nombre = input()
print("¿Cual es tu nombre?", nombre, "Tu nombre", nombre, "es el mas bonito del mundo")


# Demanem dos números enters a l'usuari
usuario1 = int(input("Introduce un numero "))
usuario2 = int(input("Introduce otro número "))
# Calculem la suma
resultat = usuario1 + usuario2
# Mostrem el resultat
print("La suma dels dos números és:", resultat)

# Demanem el nom i l'edat de l'usuari
nombre = input("Dime tu nombre ")
edad = int(input("cual es tu edad "))

# Calculem els "anys de gos" (1 any humà = 7 anys de gos)
nom = nombre
anys_de_gos = edad * 7

# Mostrem el resultat
print("Hola", nom + "! Tens", anys_de_gos, "anys en anys de gos!")

word = "Python"

