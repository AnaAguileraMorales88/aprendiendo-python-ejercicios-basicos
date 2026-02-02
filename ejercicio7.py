# Pedimos el nombre y la edad del usuario
nombre = input("Dime tu nombre: ")
edad = int(input("Dime tu edad: "))

print("Hola", nombre)

# Clasificamos según la edad
if edad < 12:
    print("Eres un niño/a")
elif edad < 18:
    print("Eres adolescente")
elif edad < 65:
    print("Eres adulto")
else:
    print("Eres adulto mayor")

# Comprobamos si puede conducir
if edad >= 18:
    print("Puedes conducir")
else:
    print("No puedes conducir")
