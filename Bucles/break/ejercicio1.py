# Escenario
# La instrucción break se implementa para salir/terminar un bucle.
# Diseña un programa que use un bucle while y le pida continuamente al usuario que ingrese una palabra,
# a menos que ingrese "chupacabra" como la palabra secreta, en cuyo caso 
# el mensaje "Has salido del bucle con éxito." debe imprimirse en pantalla y el bucle debe terminar.
# No imprimas ninguna de las palabras ingresadas por el usuario.
# Utiliza el concepto de ejecución condicional y la sentencia break.


while True:
    palabra = input("Ingresa una palabra: ")
    
    if palabra == "chupacabra":
        print("Has salido del bucle con éxito.")
        break

