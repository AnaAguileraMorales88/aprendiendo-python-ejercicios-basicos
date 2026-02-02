# Pedimos los datos al usuario
nombre = input("Dime tu nombre: ")
edad = int(input("Dime tu edad: "))
entrada = input("¿Tienes entrada? (si/no): ").lower()

print("Hola", nombre)

# Validamos la edad
if edad < 0 or edad > 120:
    print("Edad no válida")
elif edad < 16:
    print("No puedes entrar: eres menor de 16 años")
else:
    # Edad válida y mayor o igual a 16
    if entrada == "si":
        print("Puedes entrar al evento ")
    else:
        print("No puedes entrar: no tienes entrada")
