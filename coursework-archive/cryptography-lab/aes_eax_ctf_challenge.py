import time

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def juego_ctf_cifrado():
    print("Bienvenido al juego CTF de cifrado AES!")
    print("Mision: Asegurar la comunicación y recuperar la bandera.\n")

    mensaje_secreto = input("Ingresa el mensaje secreto (ej. flag{m1_pr1m3r_c1fr4d0}): ")
    mensaje_bytes = mensaje_secreto.encode("utf-8")

    clave = get_random_bytes(16)
    print("\n[!] Iniciando protocolo de cifrado AES...")
    time.sleep(1)

    cipher = AES.new(clave, AES.MODE_EAX)
    nonce = cipher.nonce
    texto_cifrado, tag = cipher.encrypt_and_digest(mensaje_bytes)

    print(f"[-] Mensaje cifrado (Hex): {texto_cifrado.hex()}")
    print(f"[-] Tag de integridad (Hex): {tag.hex()}")

    print("\n[!] Reto: Descifra el mensaje usando la clave y el nonce proporcionados.")
    accion = input("[>] ¿Deseas aplicar la clave secreta para descifrar el mensaje? (s/n): ")

    if accion.lower() == "s":
        print("\n[!] Desencriptando...")
        time.sleep(1)
        try:
            cipher_decrypt = AES.new(clave, AES.MODE_EAX, nonce=nonce)
            mensaje_recuperado = cipher_decrypt.decrypt_and_verify(texto_cifrado, tag)
            print("[+] ¡Éxito! Integridad verificada.")
            print(f"[+] Bandera recuperada: {mensaje_recuperado.decode('utf-8')}")
        except ValueError:
            print("[-] Error de descifrado: La clave es incorrecta o el mensaje fue alterado.")
    else:
        print("[-] Operación cancelada. El mensaje permanece oculto.")


if __name__ == "__main__":
    juego_ctf_cifrado()
