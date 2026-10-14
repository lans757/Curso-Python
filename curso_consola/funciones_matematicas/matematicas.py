# ============================================================================
# FUNCIONES MATEMÁTICAS — EJEMPLOS PRÁCTICOS
# ============================================================================
# Equivale a: funciones_matematicas/matematicas.php · Matematicas.cs
#             Math.* de JS · PSeInt módulo 7 (RAIZ, ABS, TRUNC, REDON, ALEATORIO)
#
# Unas pocas vienen incorporadas (round, abs, min, max, sum). El resto vive
# en dos módulos de la biblioteca estándar que hay que importar:
#   import math      -> raíces, techo, piso, pi...
#   import random    -> números al azar
# ============================================================================

import math
import random

numero = 15.185

print("round()")
# Redondea un número decimal. El segundo parámetro dice cuántos decimales
# conservar, igual que round() en PHP. (En PSeInt: REDON(x * 100) / 100.)
print(f"Redondear {numero} con 2 decimales:", round(numero, 2))
print("Redondear 7.6 a entero:", round(7.6))

# Curiosidad: Python redondea los .5 exactos hacia el número PAR más cercano
# ("redondeo del banquero"): round(2.5) da 2 y round(3.5) da 4.
print("round(2.5) =", round(2.5), "  round(3.5) =", round(3.5))

print("\nrandom.randint() (equivalente a rand())")
#   PHP:     rand(1, 10)
#   PSeInt:  ALEATORIO(1, 10)
#   Python:  random.randint(1, 10)     -> incluye el 1 y el 10
# (En C#, Next(1, 11) NO incluía el máximo; en Python sí.)
print("Número aleatorio entre 1 y 10:", random.randint(1, 10))
print("Lanzar un dado:", random.randint(1, 6))
print("Elegir al azar de una lista:", random.choice(["piedra", "papel", "tijera"]))

print("\nmath.ceil() y math.floor()")
# ceil redondea siempre HACIA ARRIBA; floor, siempre HACIA ABAJO.
# En PSeInt había que construirlos con TRUNC.
print("El techo (ceil) de 12.001 es:", math.ceil(12.001))
print("El piso (floor) de 12.999 es:", math.floor(12.999))
print("Quitar los decimales (int) de 12.999:", int(12.999))      # TRUNC en PSeInt

print("\nOtras funciones")
print("Raíz cuadrada de 49:", math.sqrt(49))          # RAIZ(49) en PSeInt
print("Valor absoluto de -8:", abs(-8))               # ABS(-8)
print("2 elevado a la 10:", 2 ** 10)                  # pow(2, 10) en PHP
print("El mayor de 4, 9 y 2:", max(4, 9, 2))
print("El menor de 4, 9 y 2:", min(4, 9, 2))

print("\nConstante math.pi (equivalente a M_PI)")
print("El valor de PI es:", math.pi)

radio = 3
print(f"Área de un círculo de radio {radio}: {math.pi * radio ** 2:.2f}")

# ----------------------------------------------------------------------------
# Ejemplo práctico: ¿cuántas mesas hacen falta?
# 23 personas, 4 por mesa -> 5.75 -> hay que redondear hacia ARRIBA.
# ----------------------------------------------------------------------------
personas = 23
por_mesa = 4
print(f"\nMesas necesarias para {personas} personas:", math.ceil(personas / por_mesa))
