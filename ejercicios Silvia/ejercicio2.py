# Escenari:
# Una botiga ofereix descomptes segons el valor total de la compra:
# Si el valor de la compra és menor o igual a 100€, el descompte és del 5%.
# Si el valor de la compra és major a 100€, el descompte és del 10%.
# El programa ha de:
# Acceptar un valor de punt flotant: el total de la compra.
# Calcular el descompte segons les regles anteriors.
# Imprimir el valor del descompte, arrodonit a dos decimals.

valor_compra = float(input("Introduce el valor de compra (en euros)..."))

if valor_compra <= 100:
    descuento = valor_compra * 0.05 # 5%

else:
    descuento = valor_compra * 0.10 # 10%

descuento = round(descuento, 2)

print("El descuento total es de", descuento, "euros.")