# ============================================================================
# CONSTANTES EN PYTHON
# ============================================================================
# Equivale a: fundamentos/constantes.php · constantes.js · Constantes.cs
#             PSeInt módulo 1 (constantes)
#
# Una constante es un valor que no debe cambiar durante la ejecución.
#
#   PHP:     define("PI", 3.1416);
#   JS:      const PI = 3.1416;
#   C#:      const double Pi = 3.1416;
#   PSeInt:  PI <- 3.1416;   (y no se reasigna)
#   Python:  PI = 3.1416     (y no se reasigna)
#
# OJO: Python NO tiene constantes de verdad. Igual que en PSeInt, es un
# ACUERDO entre programadores: si el nombre está en MAYÚSCULAS, no se toca.
# El lenguaje no lo impide; lo impide la disciplina (y las herramientas que
# revisan el código).
# ============================================================================

PI = 3.1416
print("PI:", PI)

IVA = 0.16
MAYOR_DE_EDAD = 18
PAIS = "Venezuela"

precio = 100
print("Precio con IVA:", precio + precio * IVA)
print("Mayoría de edad:", MAYOR_DE_EDAD)
print("País:", PAIS)

# ----------------------------------------------------------------------------
# Esto FUNCIONA, pero rompe el acuerdo. No lo hagas:
# ----------------------------------------------------------------------------
# PI = 3   # Python lo permite; tus compañeros de equipo, no.

# ----------------------------------------------------------------------------
# Constantes que ya trae Python
# ----------------------------------------------------------------------------
import math

print("\nmath.pi:", math.pi)        # M_PI en PHP, Math.PI en JS y C#, PI en PSeInt
print("math.e:", math.e)

# ----------------------------------------------------------------------------
# Para quien quiera que la herramienta avise: typing.Final
# No impide nada al ejecutar, pero los editores (VS Code) y los revisores de
# tipos marcan un error si alguien intenta reasignarla.
# ----------------------------------------------------------------------------
from typing import Final

NOTA_MINIMA: Final = 10
print("Nota mínima aprobatoria:", NOTA_MINIMA)
