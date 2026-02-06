import random

numero_secreto = random.randint(1, 100)
intentos = 7

print("🎮 Bienvenido al juego: Adivina el número")
print("He pensado un número entre 1 y 100")
print("Tienes 7 intentos")

while intentos > 0:
    try:
        numero = int(input(f"\nIntroduce un número (te quedan {intentos} intentos): "))
        
        if numero < 1 or numero > 100:
            print("❌ El número debe estar entre 1 y 100")
            continue

        if numero < numero_secreto:
            print("⬆️ Demasiado bajo")
        elif numero > numero_secreto:
            print("⬇️ Demasiado alto")
        else:
            print("🎉 ¡Correcto! Has adivinado el número")
            break

        intentos -= 1

    except ValueError:
        print("❌ Debes introducir un número válido")

if intentos == 0:
    print("\n💀 Te quedaste sin intentos")
    print("El número era:", numero_secreto)
