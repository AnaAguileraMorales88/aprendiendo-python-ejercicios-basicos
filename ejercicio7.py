"""Objectiu
Crear un programa senzill que permeti gestionar una llista d'alumnes mitjançant un menú interactiu.

Requisits
Utilitzar una llista per emmagatzemar els noms dels alumnes
Implementar un menú amb 4 opcions
Permetre afegir, mostrar i eliminar alumnes"""

# Llista Inicial
# El programa ha de començar amb 2 alumnes a la llista:


# Funcionalitats a Implementar
# Opció 1: Donar d'alta un alumne
# Demanar el nom del nou alumne
# Afegir-lo a la llista
# Mostrar missatge de confirmació
# Mostrar la llista actualitzada
# Opció 2: Mostrar tots els alumnes
# Llistar tots els alumnes (un per línia)
# Opció 3: Eliminar un alumne per posició
# Mostrar la llista actual d'alumnes
# Demanar la posició (número) de l'alumne a eliminar
# Eliminar l'alumne de la llista
# Mostrar missatge de confirmació
# Mostrar la llista actualitzada
# Opció 0: Sortir
# Ordena la llista de manera alfabètica
# Sortir del programa mostrant un missatge de comiat

alumnos = ["Ana" , "Silvia"];

opcion = 1

while opcion !=0:

    print("==============================")
    print("Bienvenidos al gestor de alumnos")
    print("==============================")
    print("Opción 1: Dar de alta a un alumno")
    print("Opción 2:Mostrar los alumnos")
    print("Opcion 3: Eliminar un alumno")
    print("Opcion 0: Salir")

    opcion = int(input("Dime una opción: "))

    if opcion == 1:
        nombre = input("Introduce nombre alumno: ")
        alumnos.append(nombre)
        print(alumnos)

    elif opcion == 2:
        for alumno in alumnos:
            print(alumno)

    elif opcion == 3:
        print(alumnos)
        posicion = int(input("Que posicion quiere eliminar: "))
        del alumnos[posicion]
        print("La alumna se ha eliminado correctamente. Esta es la lista actualizada: ", alumnos)

print(sorted(alumnos))

print("Gracias por utilizar el programa!")