"""Objectiu
Crear un programa que calculi el total d'una compra al supermercat utilitzant una tuple per emmagatzemar els productes i els seus preus."""

# Requisits
# Utilitzar una tuple amb tuples dins per guardar productes i preus
# Demanar a l'usuari la quantitat que vol de cada producte
# Calcular el total a pagar
# Mostrar el resultat final

# Passos a seguir
# Crear la tuple de productes:
# La tuple principal ha de contenir 4 productes
# Cada producte és una tuple amb (nom, preu)
# Productes: poma (1.20€), llet (0.85€), pa (1.50€), formatge (2.30€)

# Inicialitzar el programa:
# Inicialitzar la variable total a 0

# Processar cada producte:
# Recórrer la tuple amb un bucle for
# Per cada producte, demanar quantes unitats es volen comprar
# Multiplicar la quantitat pel preu i sumar-ho al total

# Mostrar el resultat:
# Mostrar el total final a pagar

productes = (
    ("poma", 1.20),
    ("llet", 0.85),
    ("pa", 1.50),
    ("formatge", 2.30)
)

total = 0
for producte in productes:
    nom = producte[0]
    preu = producte[1]

    quantitat = int(input("Quantes unitats de " + nom + " vols? "))

    subtotal = quantitat * preu
    total = total + subtotal

print("El total a pagar es: ", round(total ,2), "€")


