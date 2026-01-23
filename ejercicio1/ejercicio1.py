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