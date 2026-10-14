# ============================================================================
# IF CORTO (OPERADOR TERNARIO) Y VALORES POR DEFECTO
# ============================================================================
# Equivale a: condicionales/shorthand.php · Shorthand.cs
# En PSeInt no existía: había que escribir el Si ... SiNo completo.
#
# Operador ternario: una forma corta de escribir un if ... else que ELIGE UN VALOR.
#
#   PHP / JS / C#:  (condicion) ? valor_si_verdadero : valor_si_falso
#   Python:         valor_si_verdadero if condicion else valor_si_falso
#
# En Python se lee casi como una frase: "Mayor SI edad >= 18, SI NO Menor".
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Operador ternario
# ----------------------------------------------------------------------------
edad = 18

mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print("Ternario:", mensaje)

# Es exactamente lo mismo que:
if edad >= 18:
    mensaje = "Mayor de edad"
else:
    mensaje = "Menor de edad"

# ----------------------------------------------------------------------------
# 2. Valor por defecto con "or"
# PHP y C# tienen el operador ?? (si es null, usa lo otro). Python usa "or".
# ----------------------------------------------------------------------------
usuario = None
nombre_mostrado = usuario or "Invitado"
print("Con or:", nombre_mostrado)

# CUIDADO: "or" no pregunta solo por None, pregunta por CUALQUIER valor
# "falso": también reemplaza un 0 o un texto vacío.
puntos = 0
print("0 or 100       ->", puntos or 100)                           # 100 (¡ups!)

# Cuando el 0 es un valor válido, hay que preguntar por None explícitamente.
# Esto sí es el equivalente exacto de ?? en PHP y C#:
print("Preguntando por None ->", puntos if puntos is not None else 100)   # 0

# ----------------------------------------------------------------------------
# 3. Equivalente a isset(): ¿existe la clave en el diccionario?
# En PHP, isset($_POST['edad']) pregunta si llegó el dato del formulario.
# En Python los datos de un formulario llegan en un diccionario, y se usa
# .get(), que devuelve un valor por defecto si la clave no existe.
# ----------------------------------------------------------------------------
formulario = {"nombre": "Ana"}

edad_recibida = formulario.get("edad", "El usuario no estableció su edad")
print("Edad:", edad_recibida)
print("Nombre:", formulario.get("nombre", "Sin nombre"))

# También se puede preguntar directamente con "in":
if "edad" in formulario:
    print("Sí llegó la edad")
else:
    print("No llegó la edad")

# ----------------------------------------------------------------------------
# Consejo: el ternario es para elegir un VALOR entre dos. Si necesitas hacer
# varias cosas en cada camino, o encadenar tres opciones, usa el if normal:
# se entiende mejor.
# ----------------------------------------------------------------------------
