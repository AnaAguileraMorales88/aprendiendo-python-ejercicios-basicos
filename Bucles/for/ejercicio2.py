num_productos = int(input("¿Cuántos productos vas a registrar? "))

total_general = 0
producto_mas_vendido = ""
cantidad_max = 0
producto_mas_rentable = ""
ingreso_max = 0

for i in range(num_productos):
    print(f"\nProducto {i+1}")
    
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad vendida: "))
    
    total_producto = precio * cantidad
    total_general += total_producto
    
    # Producto más vendido (por cantidad)
    if cantidad > cantidad_max:
        cantidad_max = cantidad
        producto_mas_vendido = nombre
    
    # Producto que más dinero generó
    if total_producto > ingreso_max:
        ingreso_max = total_producto
        producto_mas_rentable = nombre

print("\n--- RESUMEN DE VENTAS ---")
print(f"Total general vendido: {total_general}€")
print(f"Producto más vendido (cantidad): {producto_mas_vendido}")
print(f"Producto que más dinero generó: {producto_mas_rentable}")
