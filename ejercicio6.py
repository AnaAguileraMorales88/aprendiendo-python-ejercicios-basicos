# Escenari
# Imagina una llista - no gaire llarga ni molt complicada, només una llista simple que conté alguns nombres enters. Alguns d'aquests números poden estar repetits, i aquesta és la clau. No volem cap repetició. Volem que siguin eliminats.
# La teva tasca és escriure un programa que elimini totes les repeticions de números de la llista. L'objectiu és tenir una llista en la qual tots els números apareguin no més d'una vegada.
# Nota: Assumeix que la llista original està ja dins del codi - no has d'ingressar-la des del teclat. Per descomptat, pots millorar el codi i agregar una part que pugui dur a terme una conversa amb l'usuari i obtenir totes les dades.
# Suggeriment: Et recomanem que creïs una nova llista com a àrea de treball temporal - no necessites actualitzar la llista actual.
# No hem proporcionat dades de prova, ja que seria massa fàcil. Pots usar el nostre esquelet en el seu lloc.
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# Escribe tu código aquí.
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unica_lista = []
for numeros in my_list:
    if numeros not in unica_lista:
        unica_lista.append(numeros)
my_list = unica_lista
print("La lista con elementos unicos:")
print(my_list)
# print("La lista con elementos únicos:")
# print(my_list)


