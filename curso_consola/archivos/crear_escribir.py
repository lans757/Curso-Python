# ============================================================================
# CREAR Y ESCRIBIR ARCHIVOS DE TEXTO EN PYTHON
# ============================================================================
# Equivale a: archivos/crear_escribir.php · CrearEscribir.cs
# PSeInt no puede leer ni escribir archivos.
#
# Se usa open(ruta, modo). Los modos son los MISMOS que en fopen() de PHP:
#   "w" -> escribir (write): crea el archivo; si ya existe, lo SOBRESCRIBE.
#   "a" -> agregar (append): escribe al final sin borrar lo que había.
#   "r" -> leer (read): es el modo por defecto.
#
# El bloque "with" cierra el archivo automáticamente al terminar, incluso si
# ocurre un error. Equivale a fclose() en PHP y al "using" de C#, pero sin
# tener que acordarse.
#
# encoding="utf-8" hace que las tildes y la ñ se guarden bien en cualquier
# sistema. Conviene escribirlo SIEMPRE: en Windows, si se omite, Python usa
# otra codificación y los acentos se dañan.
# ============================================================================

from datetime import datetime
from pathlib import Path

# Path(__file__).parent es la carpeta donde está este archivo .py. Así
# notas.txt se crea aquí aunque el programa se ejecute desde otra carpeta.
nombre_archivo = Path(__file__).parent / "notas.txt"

print("1. Usando open() en modo 'w' (sobrescribe)")
with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    # write() NO agrega el salto de línea: hay que escribir \n a mano.
    archivo.write("Línea 1: Hola Mundo desde Python.\n")
    archivo.write("Línea 2: Esto se escribió en modo sobrescritura.\n")
# Aquí, al salir del with, el archivo ya está cerrado.
print(f"Archivo '{nombre_archivo.name}' creado y escrito exitosamente.")

print("\n2. Usando modo 'a' (agregar al final)")
with open(nombre_archivo, "a", encoding="utf-8") as archivo:
    archivo.write("Línea 3: Esta línea fue agregada después con append.\n")
    momento = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    archivo.write(f"Línea 4: {momento} - Log de acceso.\n")
print(f"Contenido agregado a '{nombre_archivo.name}'.")

print("\n3. Escribir varias líneas de una lista")
compras = ["arroz", "harina", "aceite"]
with open(nombre_archivo, "a", encoding="utf-8") as archivo:
    for numero, producto in enumerate(compras, start=5):
        archivo.write(f"Línea {numero}: comprar {producto}\n")
print("Lista agregada.")

print("\n4. Forma abreviada: Path.write_text()")
# Equivalente a file_put_contents($archivo, $texto) de PHP: abre, escribe y
# cierra en una sola línea. OJO: sobrescribe todo el archivo.
resumen = Path(__file__).parent / "resumen.txt"
resumen.write_text("Archivo creado con la forma abreviada.\n", encoding="utf-8")
print(f"Archivo '{resumen.name}' creado con el método abreviado.")

print(f"\nRevisa el archivo '{nombre_archivo.name}' en la carpeta archivos/.")
print("Ahora ejecuta leer_archivo.py para leerlo.")
