# ============================================================================
# type(), repr() y len() — EQUIVALENTE A var_dump()
# ============================================================================
# Equivale a: var_dump.php · var_dump.js · VarDump.cs
# En PSeInt esto se hacía con la prueba de escritorio y la ejecución paso a paso.
#
# var_dump() de PHP muestra tres cosas: el TIPO, la LONGITUD y el VALOR.
# Python no tiene una función única que haga las tres, pero cada una existe:
#
#   type(x)   -> el tipo de dato
#   len(x)    -> la longitud (solo en textos, listas, diccionarios...)
#   repr(x)   -> el valor "tal cual", con comillas si es texto
#
# Aquí armamos nuestra propia función var_dump() con esas tres piezas. Es un
# buen ejemplo de algo muy común en Python: si la herramienta no existe, se
# construye en cuatro líneas.
# ============================================================================


def var_dump(variable):
    """Muestra tipo, longitud (si tiene) y valor, al estilo de PHP."""
    tipo = type(variable).__name__
    if hasattr(variable, "__len__"):
        print(f"{tipo}({len(variable)}) {variable!r}")
    else:
        print(f"{tipo}({variable!r})")


texto = "Carlos"
numero = 10
numero2 = "5"
arreglo = ["Carlos", "Cesar", "Alejandro"]
arreglo_asociativo = {"nombre": "Carlos", "edad": 20}
booleano = False
decimal = 10.5
nulo = None

print("Análisis con var_dump()")
print("Variable Texto: ", end="")
var_dump(texto)
print("Variable Numero (entero): ", end="")
var_dump(numero)
print("Variable Numero2 (texto): ", end="")
var_dump(numero2)          # OJO: es str, no int. Las comillas lo delatan.
print("Variable Decimal (float): ", end="")
var_dump(decimal)
print("Variable Nula: ", end="")
var_dump(nulo)
print("Variable Arreglo Indexado: ", end="")
var_dump(arreglo)
print("Variable Arreglo Asociativo: ", end="")
var_dump(arreglo_asociativo)
print("Variable Booleana (False): ", end="")
var_dump(booleano)

# ----------------------------------------------------------------------------
# type() solo: equivalente a gettype() de PHP y a typeof de JavaScript
# ----------------------------------------------------------------------------
print("\nDiferencia con type()")
print("type() solo devuelve el tipo, no el contenido.")
print("Tipo de texto:   ", type(texto).__name__)
print("Tipo de arreglo: ", type(arreglo).__name__)
print("Tipo de booleano:", type(booleano).__name__)

# ----------------------------------------------------------------------------
# isinstance(): preguntar "¿esto es de tal tipo?"
# ----------------------------------------------------------------------------
print("\n¿numero es un entero?   ", isinstance(numero, int))
print("¿numero2 es un entero?  ", isinstance(numero2, int))

# ----------------------------------------------------------------------------
# El truco rápido para depurar: f-string con "="
# Muestra el nombre de la variable Y su valor, sin escribirlo dos veces.
# ----------------------------------------------------------------------------
print("\nDepuración rápida con f-string:")
print(f"{numero=}  {numero2=}  {decimal=}")
