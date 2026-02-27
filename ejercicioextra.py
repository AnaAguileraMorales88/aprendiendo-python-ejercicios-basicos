"""Objetivo
Crear un programa que gestione una agenda de contactos utilizando un diccionario de Python.

Debe crear una agenda digital que permita almacenar contactos con sus números de teléfono.
El programa debe permitir añadir, ver, buscar y eliminar contactos."""

# Requisitos técnicos
# Utilizar un diccionario para almacenar los contactos

# Implementar las siguientes funciones:
# añadir_contacto() - Añade un nuevo contacto
# ver_contactos() - Ver todos los contactos
# buscar_telefon() - Busca el teléfono de un contacto
# eliminar_contacto() - Elimina un contacto
# mostrar_menu() - Muestra el menú de opciones

# Funcionalidades específicas
# 1. Añadir contacto
# Pide el nombre del contacto
# Pide el número de teléfono
# Añade el contacto al diccionario
# Muestra el diccionario actualizado

# 2. Ver todos los contactos
# Muestra todos los contactos guardados
# Formato: "El nombre es [nombre] y el teléfono es el [teléfono]"


# 3. Buscar teléfono
# Pide un nombre para buscar
# Si el nombre existe, muestra su teléfono
# Si no existe, muestra un mensaje de error

# 4. Eliminar contacto
# Pide el nombre del contacto a eliminar
# Si existe, la elimina del diccionario
# Si no existe, muestra un mensaje de error


agenda = {}

def mostrar_menu():
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Buscar teléfono")
    print("4. Eliminar contacto")
    print("5. Salir")

def agregar_contacto():
    nombre = input("Introduce un nombre: ")
    telefono = input("Introduce el numero de telefono: ")
    agenda[nombre] = telefono
    print("Numero añadido a la agenda")
    print(agenda)

def ver_contactos():
        for nombre, telefono in agenda.items():
            print("El nombre es ", nombre, "y el telefono es ", telefono)


def buscar_telefono():
    nombre = input("Introduce un contacto: ")
    if nombre in agenda:
        print("El telefono de", nombre, "es", agenda[nombre])
    else:
        print("El contacto no existe")

def eliminar_contacto():
    nombre =  input("Introduce el nombre que quieres eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto eliminado")
    else:
        print("Contacto no encontrado")

opcion = 1
while opcion != 0:
    mostrar_menu()
    opcion = input("Elige opción (1-5): ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        ver_contactos()
    elif opcion == "3":
        buscar_telefono()
    elif opcion == "4":
        eliminar_contacto()
    elif opcion == "5":
        print("¡Adiós!")
        break
    else:
        print("Opción no válida. Solo del 1 al 5.")



