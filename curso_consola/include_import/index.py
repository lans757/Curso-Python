# ============================================================================
# INCLUDE Y REQUIRE — EQUIVALENTE EN PYTHON: import
# ============================================================================
# Equivale a: include_require/index.php · IncludeUsing.cs
#             import / export de JS · "dividir en subprocesos" de PSeInt
#
# PHP:
# - include: si el archivo no existe, el programa continúa con una advertencia.
# - require: si el archivo no existe, el programa se detiene con un error fatal.
# Ambos PEGAN el contenido de un archivo dentro de otro.
#
# Python usa "import", que se parece a require (si el archivo no existe, se
# detiene con ModuleNotFoundError), pero con dos diferencias importantes:
#
# 1. NO pega el código. Ejecuta el otro archivo UNA sola vez y te da acceso a
#    sus funciones y variables a través de su nombre:  header.mostrar()
#    Por eso no hay choques de nombres entre archivos.
# 2. Aunque lo importes desde diez sitios, se ejecuta una sola vez. Es el
#    comportamiento de require_once de PHP.
#
# Cada archivo .py es un MÓDULO. Para importarlo se usa su nombre SIN ".py".
# ============================================================================

import header                      # trae el archivo header.py que está al lado
from footer import mostrar_footer  # trae solo una función de footer.py

header.mostrar_header()

print()
print("Página principal")
print("Este contenido está en index.py.")
print("Pero el encabezado y el pie de página vienen de header.py y footer.py.")
print("Título definido en header.py:", header.TITULO)
print()

mostrar_footer()

# ----------------------------------------------------------------------------
# El equivalente de "include" (seguir aunque el archivo no exista)
# ----------------------------------------------------------------------------
print()
try:
    import barra_lateral            # este archivo no existe
except ModuleNotFoundError:
    print("(El módulo 'barra_lateral' no existe; el programa continúa sin él.)")

# ----------------------------------------------------------------------------
# También se importan así los módulos que ya trae Python (la biblioteca
# estándar) y los que se instalan con pip:
#   import math            from datetime import datetime          import flask
# ----------------------------------------------------------------------------
