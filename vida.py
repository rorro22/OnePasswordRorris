import os

class Gestor:

    def __init__(self):
        pass

    def leer(self, fileName):
        try:
            with open(fileName, "rt", encoding="utf-8") as archivo:
                contenido = archivo.read()
                print("\n--- Contenido ---\n")
                print(contenido if contenido else "(archivo vacio)")
                print("\n")
        except FileNotFoundError:
            print(f"\nEl archivo {fileName} no fue encontrado en la carpeta actual.\n\n")
        except PermissionError:
            print(f"Sin permisos para leer {fileName}")
        except Exception as e:
            print(f"Error al leer: {e}")

    def grabar(self, fileName):
        try:
            texto = input("Digite el texto que desea grabar en el archivo: (Si ya existe lo puede sobrescribir.)\n")
            carpeta = os.path.dirname(fileName)

            if carpeta:
                os.makedirs(carpeta, exist_ok=True)

            with open(fileName, "wt", encoding="utf-8") as archivo:
                archivo.write(texto)
                print(f"Archivo creado/actualizado con exito: {fileName}")
        except Exception as e:
            print(f"Error al grabar: {e}")

    def editar(self, fileName):
        try:
            if not os.path.exists(fileName);
                resp = input("El archivo no existe. ¿Desea crear uno nuevo? (s/n): ").strip().lower()
                if resp != "s":
                    print("Operacion cancelada")
                    return
                
            carpeta = os.path.dirname(fileName)
            if carpeta:
                os.makedirs(carpeta, exist_ok=True)

            with open(fileName, "wt", encoding="utf-8") as archivo:
                pass

            escritura = input("\nTexto para agregar al final")
            with open(fileName, "at", encoding="utf-8") as archivo:
                archivo.write(escritura + "\n")
            print(f"Texto añadido a: {fileName}")
        except PermissionError:
            print(f"\nSin permisos para escribir: {fileName}")
        except Exception as e:
            print(f"Error al editar: {e}")

    def eliminar(self, fileName):
        try:
            if not os.path.exists(fileName):
                print(f"el archivo no existe: {fileName}")
                return
            
            resp = input(f"Seguro que deseas eliminar {fileName} ? (s/n): ".strip().lower)

            if resp == "s":
                os.remove(fileName)
                print("Archivo eliminado")
            else:
                print("Operación cancelada.")
        except PermissionError:
            print(f"Sin permisos para eliminar: {fileName}.")
        except Exception as e:
            print(f"Error al eliminar: {e}")

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