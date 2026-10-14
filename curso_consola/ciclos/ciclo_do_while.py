# ============================================================================
# EQUIVALENTE A do-while: while True + break
# ============================================================================
# Equivale a: ciclos/ciclo_do_while.php · ciclo_do_while.js · CicloDoWhile.cs
#             "Repetir ... Hasta Que" de PSeInt
#
# El do-while ejecuta el bloque SIEMPRE al menos una vez y revisa la
# condición al final. Python NO tiene do-while. Se logra lo mismo con un
# ciclo "infinito" que se rompe desde adentro:
#
#   PHP/JS/C#:  do { ... } while (condicion_para_SEGUIR);
#   PSeInt:     Repetir ... Hasta Que condicion_para_TERMINAR
#   Python:     while True:
#                   ...
#                   if condicion_para_TERMINAR:
#                       break
#
# La condición del break se escribe como en PSeInt ("hasta que"), es decir,
# al REVÉS que la del do-while de PHP.
# ============================================================================

print("--- EQUIVALENTE A DO-WHILE ---")

y = 6

# EXPLICACIÓN DEL RECORRIDO:
# 1. while True: Python entra sin preguntar nada.
# 2. Ejecución: imprime el mensaje e incrementa y.
# 3. if ... break: DESPUÉS de ejecutar el bloque se revisa si hay que salir.
#
# Nota: y empieza en 6, pero el mensaje se imprime una vez antes de que
# Python se dé cuenta de que y ya es mayor que 5.
while True:
    print(f"Este mensaje se muestra al menos una vez, y = {y}")
    y += 1
    if y > 5:
        break

# ----------------------------------------------------------------------------
# El uso más importante: VALIDAR un dato
# Se pregunta, y se vuelve a preguntar hasta que el dato sea correcto.
# (Aquí las respuestas vienen de una lista para que el ejemplo corra solo;
#  en un programa real serían: nota = float(input("Nota: ")) )
# ----------------------------------------------------------------------------
print("\n--- VALIDAR UNA NOTA ENTRE 0 Y 20 ---")
respuestas_del_usuario = [25, -3, 17]
intento = 0

while True:
    nota = respuestas_del_usuario[intento]
    intento += 1
    print(f"El usuario escribió: {nota}")

    if 0 <= nota <= 20:
        break
    print("  Nota inválida, intenta de nuevo.")

print(f"Nota guardada: {nota}")

# ----------------------------------------------------------------------------
# Otra forma válida: "preguntar una vez antes del ciclo"
# Funciona, pero repite la línea de la pregunta. Por eso se prefiere la de arriba.
#
#   nota = float(input("Nota: "))
#   while nota < 0 or nota > 20:
#       print("Nota inválida")
#       nota = float(input("Nota: "))
# ----------------------------------------------------------------------------
