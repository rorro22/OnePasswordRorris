# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import string
import hashlib
import shutil
import time

# instalar tqdm si no está
try:
    from tqdm import tqdm
except ImportError:
    print("Instalando dependencia tqdm...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tqdm"])
    from tqdm import tqdm


class Gestor:

    def __init__(self):
        pass

    def leer(self, fileName):
        try:
            with open(fileName, "rt", encoding="utf-8", errors="replace") as archivo:
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
            if not os.path.exists(fileName):
                resp = input("El archivo no existe. ¿Desea crear uno nuevo? (s/n): ").strip().lower()
                if resp != "s":
                    print("Operacion cancelada")
                    return
                carpeta = os.path.dirname(fileName)
                if carpeta:
                    os.makedirs(carpeta, exist_ok=True)
                with open(fileName, "wt", encoding="utf-8") as archivo:
                    pass  # crear vacio

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
            resp = input(f"Seguro que deseas eliminar {fileName} ? (s/n): ").strip().lower()
            if resp == "s":
                os.remove(fileName)
                print("Archivo eliminado")
            else:
                print("Operacion cancelada.")
        except PermissionError:
            print(f"Sin permisos para eliminar: {fileName}.")
        except Exception as e:
            print(f"Error al eliminar: {e}")

    # ====== soporte interno ======
    def _sha256(self, ruta, chunk=1024*1024):
        try:
            h = hashlib.sha256()
            with open(ruta, "rb") as f:
                for b in iter(lambda: f.read(chunk), b""):
                    h.update(b)
            return h.hexdigest()
        except Exception as e:
            return f"(no se pudo calcular hash: {e})"

    def _defender_path(self):
        candidatos = [
            r"C:\Program Files\Windows Defender\MpCmdRun.exe",
            r"C:\Program Files\Windows Defender\MpCmdRun\MpCmdRun.exe",
            r"C:\Program Files\Microsoft Defender\MpCmdRun.exe",
            shutil.which("MpCmdRun.exe")
        ]
        for p in candidatos:
            if p and os.path.isfile(p):
                return p
        return None

    def _scan_defender(self, ruta):
        exe = self._defender_path()
        if not exe:
            return False, "Microsoft Defender no encontrado"
        try:
            cmd = [exe, "-Scan", "-ScanType", "3", "-File", ruta, "-DisableRemediation"]
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            salida = (proc.stdout or "") + ("\n" + proc.stderr if proc.stderr else "")
            limpio = (proc.returncode == 0)
            return limpio, salida.strip()
        except Exception as e:
            return False, f"no se pudo ejecutar defender: {e}"

    def _es_sospechoso(self, ruta):
        ruta_l = ruta.lower()
        ejecutables = {".exe", ".bat", ".cmd", ".js", ".vbs", ".ps1", ".msi", ".scr", ".lnk", ".com"}
        _, ext = os.path.splitext(ruta_l)
        base = os.path.basename(ruta_l)

        doble_ext = False
        if base.count(".") >= 2:
            partes = base.split(".")
            if partes[-1] in ejecutables:
                doble_ext = True

        ubic_riesgo = any(x in ruta_l for x in [
            os.sep + "downloads" + os.sep,
            os.sep + "temp" + os.sep,
            os.sep + "appdata" + os.sep,
            os.sep + "$recycle.bin" + os.sep
        ])

        motivos = []
        if ext in ejecutables:
            motivos.append(f"extension ejecutable ({ext})")
        if doble_ext:
            motivos.append("doble extension")
        if ubic_riesgo:
            motivos.append("ubicacion de riesgo (Downloads/Temp/AppData)")

        es_riesgo = bool(motivos)
        return es_riesgo, "; ".join(motivos)

    def _detectar_discos(self):
        discos = []
        for letra in string.ascii_uppercase:
            root = f"{letra}:" + os.sep
            if os.path.isdir(root):
                discos.append(root)
        return discos

    def _buscar_archivo_en_disco(self, raiz, nombre_objetivo, ignorar_mayusculas=True, max_resultados=500, preconteo=False):
        encontrados = []
        objetivo = nombre_objetivo.lower() if ignorar_mayusculas else nombre_objetivo

        print(f"\nBuscando '{nombre_objetivo}' en {raiz} (esto puede tardar)...")
        total_dirs = None
        if preconteo:
            total_dirs = 0
            for _dp, _dn, _fn in os.walk(raiz, topdown=True):
                total_dirs += 1

        pbar = tqdm(total=total_dirs, desc=f"Escaneando {raiz}", unit="dir", dynamic_ncols=True) if total_dirs is not None else tqdm(desc=f"Escaneando {raiz}", unit="dir", dynamic_ncols=True)

        try:
            for dirpath, dirnames, filenames in os.walk(raiz, topdown=True, onerror=None):
                pbar.update(1)

                for d in dirnames:
                    dcmp = d.lower() if ignorar_mayusculas else d
                    if objetivo in dcmp:
                        ruta = os.path.join(dirpath, d)
                        encontrados.append(ruta)
                        print(f"Encontrado (carpeta): {ruta}")
                        if len(encontrados) >= max_resultados:
                            print("Limite de resultados alcanzado.")
                            return encontrados

                for f in filenames:
                    fcmp = f.lower() if ignorar_mayusculas else f
                    if objetivo in fcmp:
                        ruta = os.path.join(dirpath, f)
                        encontrados.append(ruta)
                        print(f"Encontrado: {ruta}")
                        if len(encontrados) >= max_resultados:
                            print("Limite de resultados alcanzado.")
                            return encontrados
        finally:
            pbar.close()

        if not encontrados:
            print("No se encontraron coincidencias.")
        else:
            print(f"Busqueda finalizada. Coincidencias: {len(encontrados)}")
        return encontrados

    # ====== opcion 5: buscar y escanear antes de ver ======
    def analisis(self, fileName):
        # si el usuario paso una ruta completa, usar ese flujo directo
        if fileName and os.path.isabs(fileName) and (os.path.isfile(fileName) or os.path.isdir(fileName)):
            self._analizar_y_gestionar(fileName)
            return

        # si no es ruta, ofrecer busqueda por discos
        discos = self._detectar_discos()
        if not discos:
            print("No se detectaron discos automaticamente. Ingrese una raiz (ej. C:\\).")
            raiz = input("Ruta raiz del disco: ").strip()
            discos = [raiz]

        print("\nDiscos detectados:")
        for i, d in enumerate(discos, start=1):
            print(f"{i}.- {d}")
        print("0.- Buscar en TODOS los discos listados")

        try:
            idx = int(input("Elige el disco (numero) o 0 para todos: ").strip())
        except ValueError:
            print("Opcion invalida.")
            return

        nombre_obj = fileName.strip() if fileName else input("Nombre (o parte del nombre) a buscar: ").strip()
        if not nombre_obj:
            print("Debes indicar un nombre o fragmento.")
            return

        resultados = []
        if idx == 0:
            for d in discos:
                resultados.extend(self._buscar_archivo_en_disco(d, nombre_obj, preconteo=False))
        else:
            if 1 <= idx <= len(discos):
                raiz = discos[idx - 1]
                resultados = self._buscar_archivo_en_disco(raiz, nombre_obj, preconteo=False)
            else:
                print("Indice fuera de rango.")
                return

        if not resultados:
            print("\nSin resultados.")
            crear = input("Deseas crear un archivo nuevo con ese nombre? (s/n): ").strip().lower()
            if crear == "s":
                nombre = input("Nombre del archivo (con extension): ").strip() or (nombre_obj if "." in nombre_obj else f"{nombre_obj}.txt")
                carpeta = input("Carpeta destino (Enter = Escritorio): ").strip() or os.path.join(os.path.expanduser("~"), "Desktop")
                try:
                    os.makedirs(carpeta, exist_ok=True)
                    ruta_nueva = os.path.join(carpeta, nombre)
                    texto = input("Texto inicial (puede estar vacio): ")
                    with open(ruta_nueva, "wt", encoding="utf-8") as f:
                        f.write(texto)
                    print(f"Archivo creado: {ruta_nueva}")
                except Exception as e:
                    print(f"No se pudo crear: {e}")
            return

        print("\nResultados encontrados:")
        for i, r in enumerate(resultados, start=1):
            print(f"{i}. {r}")

        sel = input("Numero del resultado a gestionar (o Enter para cancelar): ").strip()
        if not sel:
            return
        try:
            isel = int(sel)
            if not (1 <= isel <= len(resultados)):
                print("Seleccion invalida.")
                return
        except ValueError:
            print("Seleccion invalida.")
            return

        elegido = resultados[isel - 1]
        self._analizar_y_gestionar(elegido)

    def _analizar_y_gestionar(self, ruta):
        print("\nAnalizando archivo antes de abrirlo...")
        print(f"Ruta: {ruta}")

        hash256 = self._sha256(ruta)
        print(f"SHA-256: {hash256}")

        sospechoso, motivo = self._es_sospechoso(ruta)
        if sospechoso:
            print(f"Posible riesgo: {motivo}")

        limpio_def, detalle = self._scan_defender(ruta)
        if detalle:
            print("\nDefender:")
            print(detalle)

        # si sospechoso o defender no confirma, solo permitir eliminar
        if sospechoso or not limpio_def:
            print("\nPor seguridad este archivo no se mostrara. Solo puede eliminarse.\n")
            self.eliminar(ruta)
            return

        # si pasa el filtro: permitir ver/editar/eliminar
        while True:
            print("\n1.- Ver")
            print("2.- Editar (agregar)")
            print("3.- Eliminar")
            print("4.- Volver")
            op2 = input("Elige una opcion: ").strip()
            if op2 == "1":
                self.leer(ruta)
            if op2 == "2":
                self.editar(ruta)
            if op2 == "3":
                self.eliminar(ruta)
                break
            if op2 == "4":
                break


g = Gestor()
while True:

    print("Bienvenido a tu Gestor de Archivos.")
    print("1.- Leer un Archivo.")
    print("2.- Crear un Archivo.")
    print("3.- Editar un archivo.")
    print("4.- Eliminar un archivo.")
    print("5.- Buscar un Archivo y escanearlo antes de verlo.")
    print("6.- Salir.")
    try:
        op = int(input("Digite la opcion deseada: "))
    except ValueError:
        print("Opcion invalida, digite un numero.")
        continue

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
        fileName = input("Cual es el nombre del archivo que deseas buscar y analizar ? (puede ser ruta completa)\n")
        g.analisis(fileName)

    if op == 6:
        break
