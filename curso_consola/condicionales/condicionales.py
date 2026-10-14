# ============================================================================
# CONDICIONALES EN PYTHON
# ============================================================================
# Equivale a: condicionales/condicionales.php · condicionales.js
#             Condicionales.cs · PSeInt módulo 3
#
# Las condicionales permiten tomar decisiones: si una condición es verdadera
# (True), se ejecuta un bloque de instrucciones.
#
#   PSeInt:  Si edad >= 18 Entonces ... SiNo ... FinSi
#   PHP/JS/C#:  if (edad >= 18) { ... } else { ... }
#   Python:     if edad >= 18:
#                   ...
#               else:
#                   ...
#
# Tres diferencias con PHP, JS y C#:
# - La condición NO lleva paréntesis.
# - La línea del if termina en DOS PUNTOS (:).
# - No hay llaves ni "FinSi": el bloque es lo que está con SANGRÍA.
#   Si te equivocas con la sangría, el programa cambia de significado o da
#   IndentationError. En los otros lenguajes la sangría era solo estética.
# ============================================================================

# ----------------------------------------------------------------------------
# 1. if ... else
# ----------------------------------------------------------------------------
edad = 20

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# ----------------------------------------------------------------------------
# 2. Evaluación de verdad (booleanos)
# Si la variable ya es True o False, no hace falta compararla con == True.
# ----------------------------------------------------------------------------
verdadero = False

if verdadero:
    print("Esto solo se verá si la variable es True")
else:
    print("La variable es False")

# En Python también cuentan como "falso": 0, "" (texto vacío), [] (lista
# vacía), {} (diccionario vacío) y None. Todo lo demás cuenta como verdadero.
lista_de_compras = []
if not lista_de_compras:
    print("La lista de compras está vacía")

# ----------------------------------------------------------------------------
# 3. if ... elif ... else
# "elif" es la abreviatura de "else if". En PSeInt había que anidar un Si
# dentro del SiNo; aquí queda todo al mismo nivel.
# ----------------------------------------------------------------------------
mes = "Enero"

if mes == "Diciembre":
    print("Feliz Navidad")
elif mes == "Enero":
    print("Feliz Año Nuevo")
elif mes == "Julio":
    print("Feliz Julio")
else:
    print("El mes que pusiste no tiene celebración")

# ----------------------------------------------------------------------------
# 4. Condiciones compuestas con and / or / not
# ----------------------------------------------------------------------------
nota = 15

if nota < 0 or nota > 20:
    print("Nota inválida")
elif nota >= 10 and nota <= 20:
    print("Aprobado")
else:
    print("Reprobado")

# Lo mismo con una comparación encadenada (más parecido a como se lee):
if 10 <= nota <= 20:
    print("Aprobado (comparación encadenada)")

# ----------------------------------------------------------------------------
# 5. Condicionales anidados
# ----------------------------------------------------------------------------
tiene_entrada = False

if edad >= 12:
    if tiene_entrada:
        print("Puedes pasar al cine")
    else:
        print("Compra tu entrada primero")
else:
    print("Debes venir con un adulto")

# ----------------------------------------------------------------------------
# Resumen:
# - if:   se ejecuta si la condición es verdadera.
# - elif: se evalúa solo si la anterior falló.
# - else: se ejecuta si NINGUNA de las anteriores fue verdadera.
# ----------------------------------------------------------------------------
