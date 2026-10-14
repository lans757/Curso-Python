# ============================================================================
# CICLO for CON range()
# ============================================================================
# Equivale a: ciclos/ciclo_for.php · ciclo_for.js · CicloFor.cs
#             "Para i <- 1 Hasta 5 Hacer" de PSeInt
#
# Se usa cuando sabemos de antemano cuántas veces repetir.
#
#   PSeInt:  Para i <- 0 Hasta 5 Con Paso 1 Hacer ... FinPara
#   PHP:     for ($i = 0; $i <= 5; $i++) { ... }
#   Python:  for i in range(6):
#
# El for de Python NO tiene las tres partes (inicio; condición; incremento).
# En su lugar recorre una secuencia de números que fabrica range():
#
#   range(6)          -> 0, 1, 2, 3, 4, 5        (empieza en 0, NO incluye el 6)
#   range(1, 6)       -> 1, 2, 3, 4, 5           (desde 1, NO incluye el 6)
#   range(0, 11, 2)   -> 0, 2, 4, 6, 8, 10       (de 2 en 2)
#   range(5, 0, -1)   -> 5, 4, 3, 2, 1           (hacia atrás)
#
# LA TRAMPA: el último número NUNCA se incluye. "Para i <- 1 Hasta 5" de
# PSeInt se escribe range(1, 6). Es el error más común al empezar.
# ============================================================================

print("--- CICLO FOR ---")

# EXPLICACIÓN DEL RECORRIDO:
# 1. range(6) prepara los números del 0 al 5.
# 2. En cada vuelta, i toma el siguiente número.
# 3. Se ejecuta el cuerpo (lo que está con sangría).
# 4. Cuando se acaban los números, el ciclo termina solo. No hay que
#    incrementar nada a mano.
for i in range(6):
    print(f"El número es: {i}")

print("\n--- DEL 1 AL 5 (como en PSeInt) ---")
for i in range(1, 6):
    print(f"Vuelta {i}")

print("\n--- DE 2 EN 2 ---")
for i in range(0, 11, 2):
    print(i, end=" ")
print()

print("\n--- CUENTA REGRESIVA ---")
for i in range(5, 0, -1):
    print(i, end=" ")
print("¡Despegue!")

# ----------------------------------------------------------------------------
# Patrones de siempre: contador y acumulador (se inicializan ANTES del ciclo)
# ----------------------------------------------------------------------------
print("\n--- ACUMULADOR: suma del 1 al 10 ---")
suma = 0
for i in range(1, 11):
    suma += i
print("Suma:", suma)

print("\n--- TABLA DE MULTIPLICAR ---")
numero = 7
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# ----------------------------------------------------------------------------
# Ciclos anidados: por cada vuelta del externo, el interno da TODAS las suyas
# ----------------------------------------------------------------------------
print("\n--- CICLOS ANIDADOS: triángulo de asteriscos ---")
for fila in range(1, 5):
    for columna in range(fila):
        print("*", end="")
    print()

# Un detalle que en PSeInt daba problemas: si el final es menor que el
# inicio, range() simplemente no produce ningún número y el ciclo no se
# ejecuta. No cuenta hacia atrás por su cuenta.
print("\n--- range(1, 1) no ejecuta nada ---")
for i in range(1, 1):
    print("Esto no se ve")
print("(ninguna vuelta)")
