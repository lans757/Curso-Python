# ============================================================================
# RECORRER ARREGLOS CON for
# ============================================================================
# Equivale a: arreglos/recorrer_arreglo.php · recorrer_arreglos.js · RecorrerArreglo.cs
#
# El for es la forma más sencilla de recorrer una lista: se repite una vez
# por cada elemento, asignando el valor a una variable temporal. Es el
# foreach de PHP y C#.
# ============================================================================

meses = [
    "Enero", "Febrero", "Marzo", "Abril",
    "Mayo", "Junio", "Julio", "Agosto",
    "Septiembre", "Octubre", "Noviembre", "Diciembre",
]

for mes in meses:
    print("-", mes)

# ----------------------------------------------------------------------------
# Recorrer una lista de diccionarios (una "tabla")
# ----------------------------------------------------------------------------
print("\nListado de estudiantes:")
estudiantes = [
    {"nombre": "Ana", "nota": 18},
    {"nombre": "Luis", "nota": 9},
    {"nombre": "Marta", "nota": 20},
]

for estudiante in estudiantes:
    estado = "Aprobado" if estudiante["nota"] >= 10 else "Reprobado"
    print(f"  {estudiante['nombre']:<8} {estudiante['nota']:>3}  {estado}")

# ----------------------------------------------------------------------------
# Recorrer una matriz (lista de listas) con dos for anidados
# ----------------------------------------------------------------------------
print("\nMatriz de notas:")
notas = [
    [15, 12, 18],
    [9, 14, 11],
    [20, 19, 17],
]

for fila in notas:
    for nota in fila:
        print(f"{nota:>4}", end="")
    print()          # salto de línea al terminar la fila
