# ============================================================================
# GUÍA DE OPERADORES EN PYTHON
# ============================================================================
# Equivale a: fundamentos/operadores.php · operadores.js · Operadores.cs
#             PSeInt módulo 2 (operadores)
# ============================================================================

# ----------------------------------------------------------------------------
# 1. ARITMÉTICOS
# ----------------------------------------------------------------------------
a = 10
b = 3

print("1. Aritméticos")
print("10 + 3  =", a + b)       # 13
print("10 - 3  =", a - b)       # 7
print("10 * 3  =", a * b)       # 30
print("10 / 3  =", a / b)       # 3.33...  La división SIEMPRE da float
print("10 // 3 =", a // b)      # 3        División entera (sin decimales)
print("10 % 3  =", a % b)       # 1        Residuo (módulo)
print("10 ** 3 =", a ** b)      # 1000     Potencia (en PSeInt era ^)

# Diferencia importante: "//" no existe en PHP ni en JS (allá se usa
# intdiv() o Math.floor()). En PSeInt se hacía con TRUNC(a / b).

# ----------------------------------------------------------------------------
# 2. INCREMENTO Y DECREMENTO
# Python NO tiene ++ ni -- (igual que PSeInt). Se usa += 1 y -= 1.
# ----------------------------------------------------------------------------
x = 5
x += 1
print("\n2. Incremento / decremento")
print("x += 1  ->", x)          # 6
x -= 1
print("x -= 1  ->", x)          # 5

# ----------------------------------------------------------------------------
# 3. ASIGNACIÓN COMPUESTA
# ----------------------------------------------------------------------------
n = 20
print("\n3. Asignación")
n += 10
print("n += 10 ->", n)          # 30
n -= 5
print("n -= 5  ->", n)          # 25
n *= 2
print("n *= 2  ->", n)          # 50
n /= 4
print("n /= 4  ->", n)          # 12.5  (ahora n es float)
n = 20
n %= 3
print("n %= 3  ->", n)          # 2

# ----------------------------------------------------------------------------
# 4. COMPARACIÓN
# En PHP y JS existen "==" (compara valor) y "===" (compara valor y tipo).
# Python solo tiene "==" y NUNCA convierte tipos por su cuenta, así que se
# comporta como el "===" de PHP/JS. En PSeInt se comparaba con un solo "=".
# ----------------------------------------------------------------------------
n1 = 10
n2 = "10"

print("\n4. Comparación")
print('10 == "10"     ->', n1 == n2)          # False (número vs. texto)
print('10 == int("10")->', n1 == int(n2))     # True  (hay que convertir)
print("10 != 5        ->", n1 != 5)           # True  (en PSeInt era <>)
print("10 > 5         ->", n1 > 5)            # True
print("10 < 20        ->", n1 < 20)           # True
print("10 >= 10       ->", n1 >= 10)          # True
print("10 <= 5        ->", n1 <= 5)           # False

# Exclusivo de Python: comparaciones encadenadas, como en matemática.
edad = 15
print("12 <= edad < 18 ->", 12 <= edad < 18)  # True

# ----------------------------------------------------------------------------
# 5. LÓGICOS
# Se escriben con PALABRAS, igual que en PSeInt (Y, O, NO):
#   PHP / JS / C#:  &&   ||   !
#   Python:         and  or   not
# ----------------------------------------------------------------------------
v = True
f = False

print("\n5. Lógicos")
print("True and False ->", v and f)           # False
print("True or False  ->", v or f)            # True
print("not True       ->", not v)             # False

# ----------------------------------------------------------------------------
# 6. CADENAS DE TEXTO
# Se concatena con "+", como en JS, C# y PSeInt (en PHP se usa el punto).
# ----------------------------------------------------------------------------
nombre = "Juan"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido

texto = "Hola "
texto += nombre                                # "Hola Juan"

print("\n6. Cadenas")
print("Concatenar:", nombre_completo)
print("Concatenar y asignar:", texto)
print("Repetir un texto:", "ja" * 3)           # "jajaja" (solo en Python)

# ----------------------------------------------------------------------------
# 7. PERTENENCIA (no existe como operador en PHP, JS ni C#)
# "in" pregunta si un valor está dentro de un texto o de una lista.
# ----------------------------------------------------------------------------
print("\n7. Pertenencia")
print('"an" in "Juan"        ->', "an" in "Juan")
print('"Pera" in frutas      ->', "Pera" in ["Manzana", "Pera"])
print('"Kiwi" not in frutas  ->', "Kiwi" not in ["Manzana", "Pera"])

# ----------------------------------------------------------------------------
# 8. ASIGNACIÓN CONDICIONAL (se ve con calma en condicionales/shorthand.py)
# ----------------------------------------------------------------------------
usuario = None
nombre_mostrado = usuario or "Invitado"                 # como ?? de PHP/C#
es_adulto = "Sí" if edad >= 18 else "No"                # ternario

print("\n8. Asignación condicional")
print("usuario or 'Invitado' ->", nombre_mostrado)
print("Ternario              ->", es_adulto)
