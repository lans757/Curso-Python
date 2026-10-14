# Pieza compartida por los cinco archivos de soluciones: muestra la lista de
# ejercicios de un tema y ejecuta el que se elija.
#
# Es un ejemplo real de lo que enseña include_import/: en vez de copiar estas
# líneas en cada archivo, se escriben una vez y se importan.

import sys


def elegir_y_ejecutar(tema, ejercicios):
    """ejercicios es un diccionario {numero: funcion}."""
    if len(sys.argv) > 1:
        respuesta = sys.argv[1]
    else:
        print(f"Soluciones de {tema}")
        for numero, funcion in ejercicios.items():
            # La primera línea del docstring sirve de título.
            print(f"  {numero}. {funcion.__doc__.strip().splitlines()[0]}")
        respuesta = input("¿Cuál quieres ejecutar? ")

    if not respuesta.isdigit() or int(respuesta) not in ejercicios:
        sys.exit(f"Elige un número entre 1 y {len(ejercicios)}.")

    print()
    ejercicios[int(respuesta)]()
