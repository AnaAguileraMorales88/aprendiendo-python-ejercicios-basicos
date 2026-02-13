# Creem una fila de seients en un cinema (10 seients)
asientos = ["L"]*10
# Inicialment, tots els seients estan lliures
# Mostrem l'estat inicial dels seients
print("Estado inicial ", asientos)
# Algú ocupa el seient 3 (recorda que les llistes comencen des de l'índex 0)
asientos[2] = "0"
# Algú ocupa el seient 7
asientos[6] = "0"
# Mostrem l'estat actualitzat dels seients
print("Estado actualizado", asientos)