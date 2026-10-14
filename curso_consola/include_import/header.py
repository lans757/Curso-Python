# Equivalente a header.php: un archivo separado con piezas reutilizables.
# Cualquier otro archivo de esta carpeta puede usarlo con:  import header

TITULO = "Mi Proyecto Python — Curso de Consola"


def mostrar_header():
    print("======================================")
    print("  " + TITULO)
    print("======================================")


# ----------------------------------------------------------------------------
# if __name__ == "__main__":
# Lo que está dentro de este bloque SOLO se ejecuta cuando este archivo se
# corre directamente (python header.py), y NO cuando otro archivo lo importa.
# Sirve para probar un módulo sin que la prueba "se cuele" al importarlo.
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    print("Probando header.py por separado:")
    mostrar_header()
