import secrets
import string
import time

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

usuario_correcto = "Admin"

def generar_password(longitud=12):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    password = ""
    for _ in range(longitud):
        password += secrets.choice(caracteres)
    return password

def cifrar_password(password, clave):
    mensaje_bytes = password.encode("utf-8")
    cipher = AES.new(clave, AES.MODE_EAX)
    nonce = cipher.nonce
    texto_cifrado, tag = cipher.encrypt_and_digest(mensaje_bytes)
    return texto_cifrado, nonce, tag

def verificar_password(password, clave, texto_cifrado, nonce, tag):
    try:
        mensaje_bytes = password.encode("utf-8")
        cipher = AES.new(clave, AES.MODE_EAX, nonce=nonce)
        mensaje_recuperado = cipher.decrypt_and_verify(texto_cifrado, tag)
        return mensaje_recuperado == mensaje_bytes
    except ValueError:
        return False

def login():
    print("=" * 50)
    print(" SISTEMA DE LOGIN")
    print("=" * 50)
    password_generada = generar_password()
    print("\n[!] Generando contraseña aleatoria...")
    time.sleep(1)
    print(f"[+] Usuario: {usuario_correcto}")
    print(f"[+] Contraseña generada: {password_generada}")

    clave = get_random_bytes(16)
    print("\n[!] Generando clave AES...")
    time.sleep(1)

    texto_cifrado, nonce, tag = cifrar_password(password_generada, clave)
    print("[+] Contraseña cifrada correctamente.")
    print(f"[+] Password cifrado (Hex): {texto_cifrado.hex()}")
    print(f"[+] Nonce (Hex): {nonce.hex()}")
    print(f"[+] Tag (Hex): {tag.hex()}")

    print("\n" + "=" * 50)
    print(" INICIO DE SESIÓN")
    print("=" * 50)
    usuario = input("Ingrese el usuario: ")
    password = input("Ingrese la contraseña: ")

    if usuario != usuario_correcto:
        print("\n[-] Usuario incorrecto.")
        return

    print("\n[!] Verificando contraseña...")
    time.sleep(1)
    if verificar_password(password, clave, texto_cifrado, nonce, tag):
        print("[+] ¡Login exitoso!")
        print(f"[+] Bienvenido, {usuario}.")
    else:
        print("[-] Contraseña incorrecta.")

if __name__ == "__main__":
    login()
