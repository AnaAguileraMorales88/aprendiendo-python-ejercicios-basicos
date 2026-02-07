PIN_CORRECTO = "1234"
intentos = 3
saldo = 1000

# Verificación de PIN
while intentos > 0:
    pin = input("Introduce tu PIN: ")
    
    if pin == PIN_CORRECTO:
        print("✅ PIN correcto. Bienvenido.")
        break
    else:
        intentos -= 1
        print(f"❌ PIN incorrecto. Te quedan {intentos} intentos")

if intentos == 0:
    print("🚫 Tarjeta bloqueada")
else:
    # Menú del cajero
    while True:
        print("\n--- MENÚ ---")
        print("1. Ver saldo")
        print("2. Retirar dinero")
        print("3. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            print(f"💰 Tu saldo es: {saldo}€")
        
        elif opcion == "2":
            cantidad = float(input("¿Cuánto quieres retirar? "))
            
            if cantidad > saldo:
                print("❌ No tienes suficiente saldo")
            elif cantidad <= 0:
                print("❌ Cantidad no válida")
            else:
                saldo -= cantidad
                print(f"✅ Has retirado {cantidad}€. Saldo restante: {saldo}€")
        
        elif opcion == "3":
            print("👋 Gracias por usar el cajero")
            break
        
        else:
            print("❌ Opción no válida")
