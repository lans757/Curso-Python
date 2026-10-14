# ============================================================================
# RECORRIENDO ARREGLOS POR ÍNDICE (for con range y while)
# ============================================================================
# Equivale a: arreglos/recorriendo_arreglos.php · RecorriendoArreglos.cs
#             "Para i <- 1 Hasta n Hacer ... v[i]" de PSeInt
#
# Recorrer una lista usando sus posiciones numéricas, en vez del for directo.
# Es útil para entender qué hace el for "por dentro", y sigue siendo
# necesario cuando hay que MODIFICAR las casillas o comparar vecinas.
# ============================================================================

meses = [
    "Enero", "Febrero", "Marzo", "Abril",
    "Mayo", "Junio", "Julio", "Agosto",
    "Septiembre", "Octubre", "Noviembre", "Diciembre",
]

print("--- for con range(len()) ---")
# EXPLICACIÓN:
# 1. len(meses): Python cuenta 12 elementos.
# 2. range(12): produce los índices del 0 al 11.
# 3. meses[i]: accedemos al contenido usando el índice actual.
for i in range(len(meses)):
    print(f"Índice [{i}] => {meses[i]}")
print("Ideal cuando necesitas el índice para modificar o comparar casillas.")

print("\n--- while ---")
# EXPLICACIÓN:
# 1. contador = 0: definimos el punto de partida A MANO.
# 2. while: revisa si el contador sigue dentro del rango de la lista.
# 3. contador += 1: ES VITAL incrementarlo al final de cada vuelta para no
#    crear un ciclo infinito.
contador = 0
while contador < len(meses):
    print(f"Índice [{contador}] => {meses[contador]}")
    contador += 1
print("Requiere control manual del índice; útil en recorridos más complejos.")

# ----------------------------------------------------------------------------
# Cuándo SÍ hace falta el índice: modificar la lista mientras se recorre
# ----------------------------------------------------------------------------
print("\n--- Subir 2 puntos a todas las notas ---")
notas = [12, 8, 15, 9]
for i in range(len(notas)):
    notas[i] = notas[i] + 2
print(notas)

# ----------------------------------------------------------------------------
# El método burbuja del curso de PSeInt, traducido tal cual.
# No se usa en la práctica (para eso está sorted), pero es el mejor ejemplo
# de un recorrido por índice comparando casillas vecinas.
# ----------------------------------------------------------------------------
print("\n--- Burbuja a mano ---")
v = [29, 8, 15, 3, 42, 11]
n = len(v)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if v[j] > v[j + 1]:
            v[j], v[j + 1] = v[j + 1], v[j]     # intercambio sin variable auxiliar
print(v)

# Recuerda: para recorrer y solo LEER, el for directo (for mes in meses) es
# más corto y más claro. Y si además quieres el índice, enumerate().
