"""Objectiu
Crear un programa que gestioni les notes d'una classe utilitzant funcions. El programa ha de permetre 
afegir notes, veure-les, calcular la mitjana i trobar la nota més alta."""


# Funcions a implementar:
# mostrar_menu() - Mostra un menú amb 5 opcions
# afegir_nota() - Demana una nota per teclat i l'afegeix a la llista
# veure_notes() - Mostra totes les notes de la llista
# calcular_mitjana() - Calcula i mostra la mitjana de totes les notes
# trobar_maxima() - Troba i mostra la nota més alta

# Comportament esperat:
# El programa comença amb una llista buida de notes
# Mostra el menú i espera que l'usuari trii una opció (0-4)
# Es repeteix fins que l'usuari tria l'opció 0 (Sortir)
# Cada opció crida la funció corresponent
notas_alumnos = []

def mostrar_menu():
    print("Opcion 1.Agregar una nota: ")
    print("Opcion 2.Ver notas: ")
    print("Opcion 3.Calcular media: ")
    print("Opcion 4:Muestra la nota más alta: ")
    print("Opcion 0:Salir: ")

def agrega_nota():
    nota = float(input("Introduce una nota: "))
    notas_alumnos.append(nota)
    print(notas_alumnos)

def ver_notas():
    print("Notas alumnos: ", notas_alumnos)

def media_notas():
    media = sum(notas_alumnos) / len(notas_alumnos)
    print("Esta es tu nota media: ")

def nota_alta():
    maxima = max(notas_alumnos)
    print("La nota máxima es: ")

opcion = 1

while opcion != 0:
    mostrar_menu()
    opcion = int(input("Elige opcion: "))

    if opcion == 1:
        agrega_nota()

    elif opcion == 2:
        ver_notas()

    elif opcion == 3:
        media_notas()

    elif opcion == 4:
        nota_alta()
        

    elif opcion == 0:
        break

else:
    print("Tiene que ser un número del 0 al 4")

print("Has salido del programa")






