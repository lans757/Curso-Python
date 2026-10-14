# ============================================================================
# LEER ARCHIVOS DE TEXTO EN PYTHON
# ============================================================================
# Equivale a: archivos/leer_archivo.php · LeerArchivo.cs
#
#   PHP                          C#                      Python
#   ---------------------------  ----------------------  -----------------------
#   file_get_contents()          File.ReadAllText()      Path.read_text()
#   fopen()/fread()/fclose()     StreamReader            with open(...) + read()
#   file() (array de líneas)     File.ReadAllLines()     readlines() o for línea
#   file_exists()                File.Exists()           Path.exists()
# ============================================================================

import sys
from pathlib import Path

nombre_archivo = Path(__file__).parent / "notas.txt"

if not nombre_archivo.exists():
    # Equivalente a die() con mensaje.
    sys.exit(f"El archivo {nombre_archivo.name} no existe. Ejecuta primero crear_escribir.py")

print("1. Usando read_text() (la forma más fácil)")
# Lee TODO el archivo y lo devuelve como un solo texto.
contenido = nombre_archivo.read_text(encoding="utf-8")
print(contenido)

print("2. Usando open() y read() (lectura clásica)")
with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    texto = archivo.read()

if texto:
    print(texto)
else:
    print("El archivo está vacío.")

print("3. Leer línea por línea en una lista")
# Igual que file() en PHP: cada elemento de la lista es una línea.
# splitlines() quita además el salto de línea del final de cada una.
lineas = nombre_archivo.read_text(encoding="utf-8").splitlines()
for numero, linea in enumerate(lineas):
    print(f"Línea {numero}: {linea}")

print("\n4. Recorrer el archivo directamente con for (lo más eficiente)")
# Un archivo abierto se puede recorrer como una lista: entrega una línea por
# vuelta SIN cargar todo en memoria. Es lo que se usa con archivos grandes.
cantidad = 0
with open(nombre_archivo, encoding="utf-8") as archivo:
    for linea in archivo:
        cantidad += 1
        if "comprar" in linea:
            print("  Encontrada:", linea.strip())     # strip() quita el \n final
print(f"El archivo tiene {cantidad} líneas.")

# ----------------------------------------------------------------------------
# 5. ¿Y si el archivo no existe? -> FileNotFoundError
# En vez de preguntar antes con exists(), también se puede intentar y capturar.
# ----------------------------------------------------------------------------
print("\n5. Intentar abrir un archivo que no existe")
try:
    with open(Path(__file__).parent / "no_existe.txt", encoding="utf-8") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("Ese archivo no existe (error capturado, el programa sigue).")
