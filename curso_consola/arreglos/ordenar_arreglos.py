# ============================================================================
# ORDENAR ARREGLOS EN PYTHON
# ============================================================================
# Equivale a: arreglos/ordenar_arreglos.php · ordenar_arreglos.js · OrdenarArreglos.cs
# En PSeInt había que programar el método burbuja a mano (módulo 5).
#
# Python ofrece DOS formas, y la diferencia importa:
#
#   lista.sort()     -> ordena la lista ORIGINAL (como sort() de PHP y JS)
#   sorted(lista)    -> devuelve una COPIA ordenada y deja la original intacta
#
# Ante la duda, usa sorted(): no destruye el orden original.
# ============================================================================

meses_original = [
    "Enero", "Febrero", "Marzo", "Abril",
    "Mayo", "Junio", "Julio", "Agosto",
    "Septiembre", "Octubre", "Noviembre", "Diciembre",
]

# sorted() devuelve copias: no hace falta clonar la lista antes, como en PHP.
meses_asc = sorted(meses_original)                    # A-Z
meses_desc = sorted(meses_original, reverse=True)     # Z-A  (rsort en PHP)

print("Ascendente (sorted):")
for mes in meses_asc:
    print("  ^", mes)

print("\nDescendente (sorted con reverse=True):")
for mes in meses_desc:
    print("  v", mes)

print("\nLa lista original sigue igual:", meses_original[:3], "...")

# ----------------------------------------------------------------------------
# .sort(): ordena la lista original y NO devuelve nada
# ----------------------------------------------------------------------------
notas = [15, 8, 20, 12, 3]
notas.sort()
print("\nNotas ordenadas con .sort():", notas)

# Error típico:  notas = notas.sort()   -> notas queda en None.

# ----------------------------------------------------------------------------
# Ordenar con un criterio propio: el parámetro key
# key recibe una función que dice "por qué dato ordenar".
# ----------------------------------------------------------------------------
palabras = ["sol", "computadora", "casa", "programar"]
print("\nPor cantidad de letras:", sorted(palabras, key=len))

estudiantes = [
    {"nombre": "Ana", "nota": 18},
    {"nombre": "Luis", "nota": 14},
    {"nombre": "Marta", "nota": 20},
]


def obtener_nota(estudiante):
    return estudiante["nota"]


ranking = sorted(estudiantes, key=obtener_nota, reverse=True)
print("\nRanking por nota (de mayor a menor):")
for puesto, estudiante in enumerate(ranking, start=1):
    print(f"  {puesto}. {estudiante['nombre']} ({estudiante['nota']})")

# Este último ejemplo es el reto "ordenar manteniendo cada nombre junto a su
# nota" del curso de PSeInt: allá había que intercambiar dos arreglos
# paralelos a la vez dentro de la burbuja. Aquí es una línea.

# ----------------------------------------------------------------------------
# Invertir sin ordenar: reversed() o la rebanada [::-1]
# ----------------------------------------------------------------------------
print("\nLista invertida (sin ordenar):", meses_original[::-1][:3], "...")
