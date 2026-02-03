# Pedimos el número de alumnos
num_alumnos = int(input("¿Cuántos alumnos vas a ingresar? "))

# Lista para guardar los datos de cada alumno
alumnos = []

for i in range(num_alumnos):
    print(f"\nAlumno {i+1}:")
    nombre = input("Nombre: ")
    notas = []
    
    # Pedimos 3 notas por alumno
    for j in range(3):
        while True:
            nota = float(input(f"Nota {j+1} (0-10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Nota inválida. Debe estar entre 0 y 10.")
    
    # Calculamos la nota media
    media = sum(notas) / len(notas)
    
    # Clasificamos según la media
    if media < 5:
        clasificacion = "Suspenso"
    elif media < 7:
        clasificacion = "Aprobado"
    elif media < 9:
        clasificacion = "Notable"
    else:
        clasificacion = "Sobresaliente"
    
    # Guardamos los datos en la lista
    alumnos.append({"nombre": nombre, "media": round(media, 2), "clasificacion": clasificacion})

# Mostramos la tabla final
print("\n--- Resultados de los alumnos ---")
print(f"{'Nombre':<15}{'Media':<10}{'Clasificación':<15}")
print("-"*40)
for alumno in alumnos:
    print(f"{alumno['nombre']:<15}{alumno['media']:<10}{alumno['clasificacion']:<15}")
