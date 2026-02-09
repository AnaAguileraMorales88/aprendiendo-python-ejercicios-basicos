import time

USUARIO_CORRECTO = "ana"
PASSWORD_CORRECTA = "python123"

intentos = 0

while True:
    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    if usuario == USUARIO_CORRECTO and password == PASSWORD_CORRECTA:
        print("✅ Acceso concedido")
        break
    else:
        intentos += 1
        print(f"❌ Datos incorrectos. Intento {intentos}/3")

    if intentos == 3:
        print("🔒 Cuenta bloqueada. Espera 5 segundos...")
        time.sleep(5)
        intentos = 0
        print("🔓 Puedes volver a intentarlo.")
