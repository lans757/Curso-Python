# ============================================================================
# SENTENCIAS break Y continue
# ============================================================================
# Equivale a: ciclos/break_continue.php · break_continue.js · BreakContinue.cs
# En PSeInt NO existían: se resolvía con una bandera en la condición del ciclo.
#
# break:    sale por completo del ciclo.
# continue: salta el resto de la vuelta actual y pasa a la siguiente.
#
# Funcionan igual que en PHP, JS y C#.
# ============================================================================

paises = ["Mexico", "España", "Colombia", "Peru", "Argentina", "Venezuela", "Guatemala"]

# ----------------------------------------------------------------------------
# RECORRIDO CON CONTINUE: saltará España y seguirá con el resto.
# Para que continue funcione y NO imprima el país, la pregunta debe estar
# ANTES del print.
# ----------------------------------------------------------------------------
print("--- CON CONTINUE (salta España) ---")
for pais in paises:
    if pais == "España":
        continue
    print(pais)

# ----------------------------------------------------------------------------
# RECORRIDO CON BREAK: se detendrá al llegar a Colombia.
# ----------------------------------------------------------------------------
print("\n--- CON BREAK (se detiene en Colombia) ---")
for pais in paises:
    print(pais)
    if pais == "Colombia":
        break

# ----------------------------------------------------------------------------
# Con números
# ----------------------------------------------------------------------------
print("\n--- BREAK EN UN for CON range() ---")
for i in range(1, 11):
    if i == 5:
        print("Llegamos al 5, saliendo del ciclo con break.")
        break
    print(f"Número: {i}")

print("\n--- CONTINUE EN UN for CON range() ---")
for i in range(1, 6):
    if i == 3:
        print("Saltamos el número 3 con continue.")
        continue
    print(f"Número: {i}")

# ----------------------------------------------------------------------------
# EXCLUSIVO DE PYTHON: for ... else
# El bloque else de un ciclo se ejecuta SOLO si el ciclo terminó sin break.
# Es justo lo que en PSeInt se hacía con la bandera "encontrado".
# ----------------------------------------------------------------------------
print("\n--- for ... else: buscar sin bandera ---")
buscado = "Chile"

for pais in paises:
    if pais == buscado:
        print(f"{buscado} sí está en la lista")
        break
else:
    print(f"{buscado} no está en la lista")

# (Para una búsqueda tan simple basta con:  if buscado in paises: ...
#  El for...else se luce cuando la condición de búsqueda es más compleja.)
