# ============================================================================
# ARREGLOS EN PYTHON: LISTAS, DICCIONARIOS Y TUPLAS
# ============================================================================
# Equivale a: arreglos/arrays.php · arrays.js · Arrays.cs · PSeInt módulo 5
#
# Los arreglos permiten almacenar varios valores en una sola variable.
#
# PHP usa un solo tipo ("array") para todo. Python, como C#, los separa:
#
#   Lo que quieres guardar          PHP                 Python
#   -----------------------------   -----------------   --------------------
#   Lista ordenada por posición     array indexado      list  -> [ ]
#   Datos con nombre (clave-valor)  array asociativo    dict  -> { }
#   Grupo fijo que no cambia        (no existe)         tuple -> ( )
#
# En JS serían Array y Object; en C#, List<T> y Dictionary<K,V>.
#
# DIFERENCIA CON PSeInt: las posiciones empiezan en 0, no en 1.
# La primera casilla es frutas[0]. No hace falta "Dimension": la lista crece sola.
# ============================================================================

# ----------------------------------------------------------------------------
# 1. Lista (arreglo indexado, 1 dimensión)
# ----------------------------------------------------------------------------
frutas = ["Manzana", "Banana", "Naranja"]
print("Fruta en posición 0:", frutas[0])
print("Última fruta (índice -1):", frutas[-1])    # índices negativos: desde el final

frutas.append("Mango")                 # agregar al final (array_push en PHP)
frutas[1] = "Cambur"                   # modificar una casilla
print("Lista modificada:", frutas)

# Rebanadas (slices): un trozo de la lista. lista[desde:hasta], sin incluir "hasta".
print("Las dos primeras:", frutas[0:2])
print("Desde la segunda:", frutas[1:])

# ----------------------------------------------------------------------------
# 2. Diccionario (arreglo asociativo)
# ----------------------------------------------------------------------------
persona = {
    "nombre": "usuario",
    "edad": 25,
    "profesion": "Desarrollador",
}
print("\nEdad de la persona:", persona["edad"])

persona["ciudad"] = "Barinas"          # agregar una clave nueva
persona["edad"] = 26                   # modificar
print("Diccionario modificado:", persona)

# ----------------------------------------------------------------------------
# 3. Arreglo multidimensional (2D): lista de diccionarios
# Es la forma natural de representar lo que en PSeInt eran "arreglos
# paralelos" y lo que en una base de datos es una tabla con filas.
# ----------------------------------------------------------------------------
usuarios = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "usuario", "edad": 25},
]
print("\nNombre del tercer usuario:", usuarios[2]["nombre"])

# ----------------------------------------------------------------------------
# 4. Matriz (lista de listas): filas y columnas, como la matriz de PSeInt
# PSeInt: m[2, 3]      Python: m[1][2]   (dos corchetes y contando desde 0)
# ----------------------------------------------------------------------------
notas = [
    [15, 12, 18],     # estudiante 0
    [9, 14, 11],      # estudiante 1
    [20, 19, 17],     # estudiante 2
]
print("\nNota del estudiante 1 en la materia 2:", notas[1][2])

# ----------------------------------------------------------------------------
# 5. Arreglo tridimensional: Cursos -> Grupos -> Estudiantes
# ----------------------------------------------------------------------------
cursos = {
    "Programacion": {
        "GrupoA": [
            {"nombre": "Ana", "nota": 18},
            {"nombre": "Luis", "nota": 15},
        ],
        "GrupoB": [
            {"nombre": "usuario", "nota": 20},
            {"nombre": "Carlos", "nota": 17},
        ],
    },
    "Diseno": {
        "GrupoC": [
            {"nombre": "Maria", "nota": 19},
            {"nombre": "Pedro", "nota": 16},
        ],
    },
}
estudiante = cursos["Programacion"]["GrupoB"][0]["nombre"]
print("\nEstudiante del Grupo B en Programación:", estudiante)

# ----------------------------------------------------------------------------
# 6. Tupla: una lista que NO se puede modificar
# Sirve para datos que van juntos y no cambian (unas coordenadas, una fecha).
# ----------------------------------------------------------------------------
coordenadas = (8.62, -70.21)
latitud, longitud = coordenadas        # "desempaquetar" en dos variables
print("\nLatitud:", latitud, " Longitud:", longitud)
# coordenadas[0] = 9   # TypeError: las tuplas no se modifican

# ----------------------------------------------------------------------------
# Tip pedagógico: pedir una posición que no existe lanza IndexError, y pedir
# una clave que no existe lanza KeyError. (PHP solo daba una advertencia y
# JS devolvía undefined; Python, como C# y PSeInt, detiene el programa.)
# ----------------------------------------------------------------------------
