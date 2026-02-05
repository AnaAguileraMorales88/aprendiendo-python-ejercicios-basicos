import random

opciones = ["piedra", "papel", "tijeras"]
victorias_jugador = 0
victorias_ordenador = 0
ronda = 1

print("🎮 Juego: Piedra, Papel o Tijeras")
print("Gana el mejor de 3 rondas")

while victorias_jugador < 2 and victorias_ordenador < 2:
    print(f"\n--- Ronda {ronda} ---")
    jugador = input("Elige piedra, papel o tijeras: ").lower()

    if jugador not in opciones:
        print("❌ Opción no válida")
        continue

    ordenador = random.choice(opciones)
    print("El ordenador eligió:", ordenador)

    if jugador == ordenador:
        print("🤝 Empate")
    elif (
        (jugador == "piedra" and ordenador == "tijeras") or
        (jugador == "papel" and ordenador == "piedra") or
        (jugador == "tijeras" and ordenador == "papel")
    ):
        print("🎉 Ganas esta ronda")
        victorias_jugador += 1
    else:
        print("💀 Gana el ordenador")
        victorias_ordenador += 1

    ronda += 1

print("\n--- Resultado final ---")
if victorias_jugador > victorias_ordenador:
    print("🏆 ¡Has ganado el juego!")
else:
    print("🤖 El ordenador gana el juego")
