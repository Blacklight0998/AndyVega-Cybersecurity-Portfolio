import secrets
import string
import re
import getpass
import requests
import hashlib

from bs4 import BeautifulSoup


def generar_contrasena(longitud=12):

    caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
    contrasena = ""

    for _ in range(longitud):
        contrasena += secrets.choice(caracteres)

    return contrasena


def validar_usuario(usuario):

    patron = r"^[A-Za-z]+@[A-Za-z]+\.[A-Za-z]+$"

    if re.match(patron, usuario):
        return True
    else:
        return False


def hash_contrasena():

    contrasena = getpass.getpass("Ingrese la contraseña a convertir en hash: ")

    contrasena_bytes = contrasena.encode("utf-8")

    hash_contrasena = hashlib.sha256(contrasena_bytes).hexdigest()

    print("Hash de la contraseña:", hash_contrasena)


def web_scraping():

    url = "https://www.walmart.co.cr/cerveza-lata-pilsen-710ml-4/p"

    respuesta = requests.get(url)

    if respuesta.status_code == 200:

        soup = BeautifulSoup(respuesta.content, "html.parser")

        print("\n---------------------------")
        print("Web Scraping de Walmart")
        print("---------------------------")

        nombre = soup.find("h1")

        if nombre:
            print("Nombre del producto:", nombre.get_text(strip=True))

        texto = soup.get_text(" ", strip=True)

        precio = re.search(r"₡[\d.]+", texto)

        if precio:
            print("Precio del producto:", precio.group())

        texto = soup.get_text(" ",strip=True)

        precios = re.findall(r"₡[\d.]+",texto)

        if precios:
            print("Precio original:", precios[0])

        if len(precios) > 1:
            print("Precio rebajado:", precios[1])

        descuento = re.search(r"-\s?\d+%",texto)

        if descuento:
            print("Descuento:",descuento.group())

        descripcion = soup.find(
            string=re.compile("Producto con venta restringida"))

        if descripcion:
            print("\nDescripción:")
            print(descripcion.strip())

    else:

        print("Error al acceder a los datos del producto.")


def menu():
    opcion = ""
    while opcion != "0":
        print("\nSeleccione una opción:")
        print("1. Generar hash de contraseña")
        print("2. Web Scraping ")
        print("0. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            hash_contrasena()

        elif opcion == "2":
            web_scraping()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


def login():

    print("Bienvenido al sistema de inicio de sesión.")
    contrasena_generada = generar_contrasena()

    print("Su contraseña generada es:", contrasena_generada)

    usuario = input("Ingrese su usuario (correo electrónico): ")

    while not validar_usuario(usuario):
        print("Usuario inválido. Debe ser un correo electrónico válido.")

        usuario = input("Ingrese su usuario (correo electrónico): ")

    print("Usuario válido. Acceso concedido.")

    contrasena_ingresada = getpass.getpass("Ingrese su contraseña: ")
    while not contrasena_ingresada == contrasena_generada:
        print("Contraseña incorrecta. Acceso denegado.")
        contrasena_ingresada = getpass.getpass("Ingrese su contraseña: ")
    else:
        print("Contraseña correcta. Acceso concedido.")
        menu()


if __name__ == "__main__":
    login()
