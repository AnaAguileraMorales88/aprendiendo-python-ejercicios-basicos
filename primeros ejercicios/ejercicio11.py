# Pedimos cuántos días se van a analizar
num_dias = int(input("¿Cuántos días quieres analizar? "))

# Listas para guardar los datos
temp_min = []
temp_max = []
temp_media = []
lluvia = []

for dia in range(1, num_dias + 1):
    print(f"\nDía {dia}")

    # Validamos temperaturas
    while True:
        minima = float(input("Temperatura mínima (-50 a 60): "))
        maxima = float(input("Temperatura máxima (-50 a 60): "))

        if minima < -50 or maxima > 60:
            print("Error: temperaturas fuera de rango.")
        elif maxima < minima:
            print("Error: la máxima no puede ser menor que la mínima.")
        else:
            break

    # Validamos lluvia
    while True:
        llovio = input("¿Llovió este día? (si/no): ").lower()
        if llovio == "si" or llovio == "no":
            break
        else:
            print("Respuesta inválida. Escribe 'si' o 'no'.")

    # Guardamos datos
    temp_min.append(minima)
    temp_max.append(maxima)
    temp_media.append((minima + maxima) / 2)
    lluvia.append(llovio)

# Resultados diarios
print("\n--- Temperaturas medias por día ---")
for i, media in enumerate(temp_media):
    print(f"Día {i+1}: {media:.2f}°C")

# Día más caluroso y más frío
dia_caluroso = temp_max.index(max(temp_max)) + 1
dia_frio = temp_min.index(min(temp_min)) + 1

# Media general
media_general = sum(temp_media) / len(temp_media)

# Días con y sin lluvia
dias_lluvia = lluvia.count("si")
dias_secos = lluvia.count("no")

print("\n--- Resumen semanal ---")
print(f"Día más caluroso: Día {dia_caluroso} ({max(temp_max)}°C)")
print(f"Día más frío: Día {dia_frio} ({min(temp_min)}°C)")
print(f"Media general de temperatura: {media_general:.2f}°C")
print(f"Días con lluvia: {dias_lluvia}")
print(f"Días sin lluvia: {dias_secos}")

# Mensaje final
if dias_lluvia > dias_secos:
    print("Semana lluviosa ☔")
elif dias_secos > dias_lluvia:
    print("Semana seca ☀️")
else:
    print("Semana equilibrada 🌤️")
