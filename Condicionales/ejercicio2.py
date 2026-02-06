# Escenario:
# Una tienda ofrece descuentos según el valor total de la compra:
# Si el valor de la compra es menor o igual a 100€, el descuento es del 5%.
# Si el valor de la compra es mayor a 100€, el descuento es del 10%.
# El programa debe:
# Aceptar un valor de punto flotante: el total de la compra.
# Calcular el descuento según las reglas anteriores.
# Imprimir el valor del descuento, redondeado a dos decimales.


valor_compra = float(input("Introduce el valor de compra (en euros)..."))

if valor_compra <= 100:
    descuento = valor_compra * 0.05 # 5%

else:
    descuento = valor_compra * 0.10 # 10%

descuento = round(descuento, 2)

print("El descuento total es de", descuento, "euros.")