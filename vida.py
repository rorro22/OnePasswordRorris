import os

class Gestor:

    def __init__(self):
        pass

    def leer(self, fileName):
        with open(fileName, "r") as archivo:
            print(archivo.read())

    def grabar(self, fileName):
        with open(fileName, "wb"):
            print(fileName)

    def editar(self, fileName):
        with open(fileName, "a") as archivo:
            texto = input("Escribe el texto que deseas que tenga el archivo: ")
            archivo.write(f"\n{texto}")
            print(archivo)

    def eliminar(self, fileName):
        os.remove(fileName)

    def analisis(self, fileName):
        pass

g = Gestor()
while True:

    print("Bienvenido a tu Gestor de Archivos.")
    print("1.- Leer un Archivo.")
    print("2.- Crear un Archivo.")
    print("3.- Editar un archivo.")
    print("4.- Eliminar un archivo.")
    print("5.- Buscar un Archivo y escanearlo antes de verlo.")
    print("6.- Salir.")
    op = int(input("Digite la opción deseada: "))

    if op == 1:
        fileName = input("Cual es el nombre del archivo que deseas buscar ?\n")
        g.leer(fileName)

    if op == 2:
        fileName = input("Cual es el nombre del archivo que deseas grabar ?\n")
        g.grabar(fileName)

    if op == 3:
        fileName = input("Cual es el nombre del archivo que deseas editar ?\n")
        g.editar(fileName)

    if op == 4:
        fileName = input("Cual es el nombre del archivo que deseas eliminar ?\n")
        g.eliminar(fileName)

    if op == 5:
        # fileName = input("Cual es el nombre del archivo que deseas buscar y analizar ?\n")
        # g.analisis(fileName)
        print("\nPor el momento se esta trabajando tanto en hacer mas robusto el programa como en crear esta opcion. Gracias por la espera.\n")
        pass

    if op == 6:
        break