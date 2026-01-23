print("hola")
print(12)
print("12")
print("coche","moto")


print(11_111_111)
print(0o123)
print(-222 -111)
print(0x123)
print(3E8)

print('Me gusta "Big Bang Theory"')

print(type("Hola"))
print(len([1, 2, 3,4,5]))

print(True > False) #False se considera como 0 True se considera como 1
print(True < False)  #Python convierte True a 1 y False a 0
#En resumen: los booleanos en Python son números enteros bajo el capó, donde False = 0 y True = 1. Por eso se pueden usar en comparaciones, sumas, restas, etc.

print([True, False, True].count(True)) # Cuenta cuántos True hay → 2


for i in range(9):
    if i % 2 == True:  # equivale a if i % 2 == 1
        print(i, "es impar")

print(2 + 2)

a = 10
b = 4
print(a - b)

a = 10
b = 2
print(a / b) #Una / Devuelve siempre un número decimal, aunque la división sea exacta.

a = 10
b = 3
print(a // b) #Dos // Devuelve solo la parte entera del resultado (sin decimales).