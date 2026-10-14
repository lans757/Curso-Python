# ============================================================================
# CICLO while
# ============================================================================
# Equivale a: ciclos/ciclo_while.php · ciclo_while.js · CicloWhile.cs
#             "Mientras ... Hacer" de PSeInt
#
# Ejecuta un bloque MIENTRAS una condición sea verdadera. La condición se
# revisa ANTES de entrar: si desde el principio es falsa, el bloque no se
# ejecuta ni una vez.
#
#   PSeInt:  Mientras x <= 5 Hacer ... FinMientras
#   PHP/JS/C#:  while (x <= 5) { ... }
#   Python:     while x <= 5:
# ============================================================================

print("--- CICLO WHILE ---")

x = 1

# EXPLICACIÓN DEL RECORRIDO:
# 1. Definición inicial: una variable de control (x = 1).
# 2. Evaluación: antes de entrar, Python pregunta: ¿x <= 5?
# 3. Ejecución: si la respuesta es sí, ejecuta el print.
# 4. Actualización (x += 1): es CRUCIAL cambiar la variable dentro del ciclo
#    para que en algún momento la condición sea falsa y el ciclo termine.
while x <= 5:
    print(f"Iteración número: {x}")
    x += 1

# ----------------------------------------------------------------------------
# CICLO INFINITO: si olvidas x += 1, la condición nunca cambia y el programa
# no termina. Para detenerlo en la terminal se pulsa Ctrl + C.
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Cuándo conviene while en vez de for: cuando NO sabes cuántas vueltas serán.
# ----------------------------------------------------------------------------
print("\n--- ¿Cuántas veces hay que duplicar 1 para pasar de 100? ---")
valor = 1
veces = 0
while valor <= 100:
    valor *= 2
    veces += 1
print(f"Se duplicó {veces} veces y llegó a {valor}")

# ----------------------------------------------------------------------------
# Bandera: una variable booleana que avisa cuándo parar
# ----------------------------------------------------------------------------
print("\n--- BÚSQUEDA CON BANDERA ---")
numeros = [4, 9, 15, 21, 30]
buscado = 15
encontrado = False
posicion = 0

while posicion < len(numeros) and not encontrado:
    if numeros[posicion] == buscado:
        encontrado = True
    else:
        posicion += 1

if encontrado:
    print(f"El {buscado} está en la posición {posicion}")
else:
    print(f"El {buscado} no está en la lista")

# En PSeInt esta bandera era obligatoria porque no existía "break".
# En Python existe; se ve en break_continue.py.
