# Pedimos al usuario cuántos días quiere registrar
num_dias = int(input("¿Cuántos días quieres registrar la temperatura? "))

# Listas para guardar temperaturas
temp_minimas = []
temp_maximas = []
temp_medias = []

for dia in range(1, num_dias + 1):
    print(f"\nDía {dia}:")
    
    # Pedimos la temperatura mínima
    while True:
        min_temp = float(input("Temperatura mínima: "))
        max_temp = float(input("Temperatura máxima: "))
        if max_temp >= min_temp:
            break
        else:
            print("Error: la temperatura máxima debe ser mayor o igual que la mínima. Inténtalo de nuevo.")
    
    # Guardamos las temperaturas
    temp_minimas.append(min_temp)
    temp_maximas.append(max_temp)
    
    # Calculamos la media del día
    media_dia = (min_temp + max_temp) / 2
    temp_medias.append(media_dia)

# Mostramos resultados
print("\n--- Resumen de temperaturas ---")
for i, media in enumerate(temp_medias):
    print(f"Día {i+1}: Temperatura media = {media:.2f}°C")

# Temperatura más alta
max_temp_total = max(temp_maximas)
dia_max = temp_maximas.index(max_temp_total) + 1

# Temperatura más baja
min_temp_total = min(temp_minimas)
dia_min = temp_minimas.index(min_temp_total) + 1

# Media general de todas las temperaturas
media_general = sum(temp_medias) / len(temp_medias)

print("\n--- Estadísticas generales ---")
print(f"Temperatura más alta: {max_temp_total}°C (Día {dia_max})")
print(f"Temperatura más baja: {min_temp_total}°C (Día {dia_min})")
print(f"Media general de todas las temperaturas: {media_general:.2f}°C")
