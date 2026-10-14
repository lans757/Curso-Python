# ============================================================================
# sys.exit() — EQUIVALENTE A die() / exit()
# ============================================================================
# Equivale a: die.php · Die.cs
# En PSeInt no existía: se evitaba seguir con un "Si" que envolvía el resto.
#
# ¿QUÉ HACE?
# 1. Detiene la ejecución del programa de inmediato.
# 2. No se ejecuta NINGUNA línea que esté por debajo.
#
# CASOS DE USO COMUNES:
# - Depuración: detener el programa y revisar el estado de las variables.
# - Seguridad: cortar si no se cumplen ciertos requisitos.
# - Errores graves: si falla la conexión a la base de datos, no tiene sentido seguir.
#
# Diferencia con PHP: die() es una función del lenguaje. En Python hay que
# importar el módulo "sys" y llamar sys.exit(). Si se le pasa un texto, lo
# muestra como mensaje de error y el programa termina con código 1.
# ============================================================================

import sys

print("Soy un print")
print("Hola Mundo")

# Ejemplo de exit con mensaje (comentado):
# sys.exit("El programa se detuvo por un error crítico.")

sys.exit()

# Esta línea NUNCA se ejecuta: el programa ya terminó en la línea anterior.
print("Esto no se verá en pantalla")
