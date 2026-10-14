# ============================================================================
# CONTAR ELEMENTOS DE UN ARREGLO
# ============================================================================
# Equivale a: arreglos/contar_elementos_arreglos.php · ContarElementosArreglos.cs
# En PSeInt no existía: había que guardar el tamaño en una variable "n".
#
#   PHP:     count($meses)
#   JS:      meses.length
#   C#:      meses.Length  /  lista.Count
#   Python:  len(meses)
#
# len() es una función general: sirve igual para listas, diccionarios y textos.
# ============================================================================

meses = [
    "Enero", "Febrero", "Marzo", "Abril",
    "Mayo", "Junio", "Julio", "Agosto",
    "Septiembre", "Octubre", "Noviembre", "Diciembre",
]

# 1. Contar elementos totales
print("Total de meses:", len(meses))

# 2. Acceder al último elemento
# Como las posiciones empiezan en 0, el último índice es (total - 1).
ultimo_indice = len(meses) - 1
print("El último mes del año es:", meses[ultimo_indice])

# Tip: en Python existe el índice negativo. -1 significa "el último",
# -2 "el penúltimo"... (equivale al ^1 de C#; PHP y JS no lo tienen).
print("Con el índice -1:", meses[-1])
print("El penúltimo:", meses[-2])

# 3. len() con otros tipos
persona = {"nombre": "Ana", "edad": 20}
print("\nClaves del diccionario:", len(persona))
print("Letras de 'Barinas':", len("Barinas"))

# 4. Contar cuántas veces aparece un valor
notas = [15, 10, 18, 10, 20, 10]
print("\n¿Cuántas veces aparece el 10?", notas.count(10))

# 5. Funciones que resumen una lista de números
# En PSeInt cada una era un ciclo con su acumulador.
print("Suma:", sum(notas))
print("Mayor:", max(notas))
print("Menor:", min(notas))
print("Promedio:", sum(notas) / len(notas))

# Tip pedagógico:
# Si intentamos acceder a meses[12] obtendríamos un IndexError, porque el
# conteo empieza en 0 y termina en 11. Por eso se usa len(meses) - 1, o
# directamente meses[-1].
