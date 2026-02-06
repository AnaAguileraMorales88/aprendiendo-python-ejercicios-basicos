"""Escribe un programa de dos líneas que lea un número entero e imprima True si el número es par y mayor que 20. En cualquier otro caso debe imprimir False.
No uses if, solo operadores de comparación y lógicos."""

n = int(input())
print(n > 20 and n % 2 == 0)


"""Escribe un programa de dos líneas que lea un número entero e imprima True si el número es negativo o mayor que 100. En cualquier otro caso debe imprimir False.
No uses if."""

n = int(input())
print(n < 0 or n > 100)
