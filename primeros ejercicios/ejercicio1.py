print("hola")
print(12)
print("12")
print("coche","moto")


print(11_111_111)
print(0o123)
print(-222 -111)
print(0x123)
print(3E8)

print('Me gusta "Big Bang Theory"')

print(type("Hola"))
print(len([1, 2, 3,4,5]))

print(True > False) #False se considera como 0 True se considera como 1
print(True < False)  #Python convierte True a 1 y False a 0
#En resumen: los booleanos en Python son números enteros bajo el capó, donde False = 0 y True = 1. Por eso se pueden usar en comparaciones, sumas, restas, etc.

print([True, False, True].count(True)) # Cuenta cuántos True hay → 2


for i in range(9):
    if i % 2 == True:  # equivale a if i % 2 == 1
        print(i, "es impar")

print(2 + 2)

a = 10
b = 4
print(a - b)

a = 10
b = 2
print(a / b) #Una / Devuelve siempre un número decimal, aunque la división sea exacta.

a = 10
b = 3
print(a // b) #Dos // Devuelve solo la parte entera del resultado (sin decimales).

# Truco mental rápido
# / → piensa en matemáticas normales
# // → piensa en “suelo” (floor)
# % → piensa en “lo que falta para llegar al siguiente múltiplo”

edad = 20
tiene_carnet = True

print(edad >= 18 and tiene_carnet)

print ((2 ** 4), (2 * 4.), (2 *4))

ALICIA = "coches" 
Alicia = "colores"
alicia = "frutas"

print(Alicia) #Imprime el que está escrito igual

var = 1
nombre_cliente = "Ana Aguilera"
cuenta_bancaria = 1000.0

print(var, nombre_cliente, cuenta_bancaria)

var = "3.8.5"
print("Python version: " + var + "\n" "otra linea")

# Imagina que estem fent una recepta per a fer galetes.
# Suposem que tens 2 galetes i el teu amic et dona 3 més.
# Llavors, quantes galetes tens en total?
# Codi:

galetes = 2
galetes += 3
print("Tinc", galetes, "galetes") # Para ahorrar código sería galetes 2 + 3 directamente


# Imagina que tens 5 galetes i decideixes menjar-te 2.
# Quantes galetes et queden?
# Codi:

galetes = 5
galetes -= 2
print(galetes)


# Ara, imagina que vols fer 3 caixes de galetes, i en cada caixa poses 4 galetes. 
# Quantes galetes tens en total?
# Codi:

caixes = 3
galetes_caixes = 4
total_galetes = caixes * galetes_caixes
print(total_galetes) 

# I si tens 12 galetes i les vols compartir entre 4 amics, quantes galetes li toquen a cadascun?
# Codi:

galetes = 12
amics = 4
galetas_amics = galetes // amics
print(galetas_amics)

#Crear les variables: Juan, Maria, i Adán

#Una vegada emmagatzemats els números en les variables, imprimir les variables en una línia, i separar cadascuna d'elles amb una coma;

#Després s'ha de crear una nova variable anomenada total_pomes i s'ha d'igualar a la suma de les tres variables anteriors;


"""Escenari
A continuació una història:
Érase una vegada en la Terra de les Pomes, Juan tenia tres pomes, María tenia cinc pomes, i Adán tenia sis pomes. Tots eren molt feliços i van viure per moltíssim temps. Fi de la Història.

La teva tasca és:
Crear les variables: Juan, Maria, i Adán;
Assignar valors a les variables. El valor ha de ser igual al nombre de pomes que cada qui tenia;
Una vegada emmagatzemats els números en les variables, imprimir les variables en una línia, i separar cadascuna d'elles amb una coma;
Després s'ha de crear una nova variable anomenada total_apples i s'ha d'igualar a la suma de les tres variables anteriors;
Imprimeix el valor emmagatzemat en total_apples en la consola;"""

Juan =  3
María = 5
Adán = 6
print(Juan, María, Adán, sep=", ")

total_apples = Juan + María + Adán
print("El total de les pomes es", total_apples)

pomes = 100

pomes += 50

pomes -= 30

pomes -= 10

print(pomes)

"""Escenari
Milles i quilòmetres són unitats de longitud o distància.
Tenint al cap que 1 milla equival aproximadament a 1.61 quilòmetres, complementa el programa en l'editor perquè converteixi de:
Milles a quilòmetres;
Quilòmetres a milles.
No s'ha de canviar el codi existent. Escriu el teu codi en els llocs indicats amb ###. Prova el teu programa amb les dades que han estat proveïts en el codi font.
Posa molta atenció al que aquesta ocorrent dins de la funció print(). Analitza com és que es proveeixen múltiples arguments per a la funció, i com és que es mostra el resultat.
Nota que alguns dels arguments dins de la funció print() són cadenes (per exemple, "milles són", i altres són variables (per exemple, milers)."""

milles = 10
km = 5

print("Mi nombre es", "Ana", end=" * ")
print("Aguilera", end="...") #end coge la línea siguiente y te la pone en la misma línea, siempre se pone al final de cada print
print("Morales")


# Imaginem que volem crear una llista d'ingredients en una sola línia
print("Els ingredients són: ", end="")
# Farina
print("Harina,", end=" ")
# Sucre
print("azucar,", end=" ")
# Ous
print("huevos,", end=" ")
# Llet
print("y leche")


# Farem una truita de patates, passos per fer-la...
print("Passos per fer una truita: ", end="")
# 1. Trencar els ous ->
print("1. Trencar els ous", end=" -> ")
# 2. Barrejar amb sal ->
print("2. Barrejar amb sal", end=" -> ")
# 3. Escalfar la paella ->
print("3. Escalfar la paella", end=" -> ")
# 4. Coure la truita.
print("4. Coure la truita.")

print("Mi", "nombre", "es", sep="_", end="*") #sep separa las palabras de la misma frase por lo que le pongas entre comillas
print("nombre", "apellido", sep="-")


print("Ana " * 3)
