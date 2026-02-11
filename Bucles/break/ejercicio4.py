num_transacciones = int(input("¿Cuántas transacciones vas a revisar? "))

fraude_detectado = False

for i in range(num_transacciones):
    monto = float(input(f"Transacción {i+1} - Monto: "))
    
    if monto > 10000:
        print("🚨 Alerta: posible fraude detectado.")
        print(f"Transacción sospechosa en la posición {i+1}")
        fraude_detectado = True
        break

if not fraude_detectado:
    print("✅ Todas las transacciones son normales.")
